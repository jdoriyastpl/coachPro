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

class CoursesListView(ListView):
    model = Courses

    def get_queryset(self):
        return Courses.objects.order_by('name')

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
