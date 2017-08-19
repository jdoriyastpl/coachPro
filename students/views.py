from django.shortcuts import render,redirect,get_object_or_404
from students.models import Students,StudentPaymentDetail
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from students.forms import StudentForm,StudentPaymentDetailForm
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
from students.signals import pending_payment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    paginate_by = 15
    def get_queryset(self):
        return Students.objects.filter(created_date__lte=timezone.now()).filter(user = self.request.user).order_by('-created_date')


class StudentsDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'students_details'
    login_url = 'login'
    model = Students
    template_name = 'students/profile.html'

class StudentsUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    redirect_field_name = 'students/students_list.html'
    form_class = StudentForm
    redirect_field_name = 'students/students_detail.html'
    model = Students
    def get_form_kwargs(self):
            kwargs = super(StudentsUpdateView, self).get_form_kwargs()
            kwargs['user'] = self.request.user
            return kwargs
    # def post(self, request, **kwargs):
    #     request.POST['user'] = request.user
    #     return super(StudentsUpdateView, self).post(request, **kwargs)


class StudentPaymentCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = StudentPaymentDetail
    form_class = StudentPaymentDetailForm
    template_name = 'students/studentpaymentdetail_form.html'
    redirect_field_name = 'students/paymentHistoryList_form.html'

    def form_valid(self,form):
        student = form.cleaned_data.get('Student_Enrol_id')
        try:
            student_name = Students.objects.get(student_Id=student)
        except:
            messages.error(self.request,"Student Id is not matching with our records, Please search for verification")
            return self.form_invalid(form)
        # Intial Garbage code during debugging, will be removed in screening
        # form.save()
        # last_expected_payment_dates = StudentPaymentDetail.objects.values_list("next_payment_date", flat=True).filter(student=student_name).order_by("-pk")
        # print(len(last_expected_payment_dates))
        # print(last_expected_payment_dates)
        # if len(last_expected_payment_dates)==0:
        #     pass
        # elif len(last_expected_payment_dates)>1:
        #     last_expected_payment_date = last_expected_payment_dates[1]
        #     if datetime.now() >=last_expected_payment_date:
        #         print("Student Payment is pending")
        #         pending_payment.send(sender=StudentPaymentDetail,student=student)
        # print(last_expected_payment_date)

        # if datetime.now() >=next_payment_date:
        #     print("yes we are passed")
        #     pending_payment.send(sender=StudentPaymentDetail,student=student)
        return super(StudentPaymentCreateView,self).form_valid(form)
    # def get_form_kwargs(self):
    #     kwargs = super(StudentPaymentCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

class StudentPaymentHistoryListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = StudentPaymentDetail
    form_class = StudentPaymentDetailForm
    template_name = 'students/paymentHistoryList_form.html'
    paginate_by = 15

    def get_queryset(self):
        filter =self.kwargs['Student_Enrol_id']
        #debugging url param
        # print(filter)
        return StudentPaymentDetail.objects.filter(Student_Enrol_id=filter).order_by('-payment_date')
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StudentPaymentHistoryListView, self).get_context_data(**kwargs)
    #     q = self.request.GET.get("student")
    #     context['student'] = q
    #     return context
