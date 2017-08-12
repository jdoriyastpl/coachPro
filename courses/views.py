from django.shortcuts import render,redirect,get_object_or_404
from courses.models import Courses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.forms import CoursesForm
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
class CoursesCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    form_class = CoursesForm
    redirect_field_name = 'courses/courses_list.html'
    model = Courses
    # valid the form from using mixins and add user to course
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CoursesCreateView,self).form_valid(form)


class CoursesListView(ListView):
    model = Courses

    def get_queryset(self):
        return Courses.objects.filter(user=self.request.user).order_by('name')

class CoursesDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'courses_details'
    login_url = 'login'
    model = Courses
    template_name='courses/courses_details.html'

class CoursesUpdateView(LoginRequiredMixin,UpdateView):
    login_url='login'
    form_class = CoursesForm
    redirect_field_name='courses/courses_details.html'
    model =Courses
