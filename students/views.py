from django.shortcuts import render,redirect,get_object_or_404
from students.models import Students,StudentPaymentDetail
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from students.forms import StudentForm,StudentPaymentDetailForm
from django.utils import timezone
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# Create your views here.

class StudentsCreateView(LoginRequiredMixin,CreateView):
    # template_namev= 'student_form.html'
    login_url = 'login'
    form_class = StudentForm
    redirect_field_name = 'students/students_list.html'
    model = Students

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(StudentsCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(StudentsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class StudentsListView(LoginRequiredMixin,ListView):
    model = Students

    def get_queryset(self):
        return Students.objects.filter(created_date__lte=timezone.now()).filter(user = self.request.user).order_by('-created_date')

class StudentsDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'students_details'
    login_url = 'login'
    model = Students
    template_name = 'students/students_detail.html'

class StudentsUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    # redirect_field_name = 'students/students_list.html'
    form_class = StudentForm
    redirect_field_name = 'students/students_detail.html'
    model = Students
    def post(self, request, **kwargs):
        request.POST['user'] = request.user
        return super(StudentsUpdateView, self).post(request, **kwargs)


class StudentPaymentCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = StudentPaymentDetail
    form_class = StudentPaymentDetailForm
    template_name = 'students/studentpaymentdetail_form.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(StudentPaymentCreateView,self).form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(StudentPaymentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
