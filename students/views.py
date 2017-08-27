from django.shortcuts import render,redirect,get_object_or_404
from students.models import Students,StudentPaymentDetail,SendNotification
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from students.forms import StudentForm,StudentPaymentDetailForm
from django.utils import timezone
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from datetime import datetime
from courses.models import  Courses
from django.db.models import Sum
import weasyprint
from django.conf import settings
from django.http import HttpResponse
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

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    login_url= 'login'
    success_message = "Deleted Successfully"
    success_url = reverse_lazy('students:student_list')

    def get_queryset(self):
        return Students.objects.filter(created_date__lte=timezone.now()).filter(user = self.request.user).order_by('-created_date')


class StudentPaymentCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = StudentPaymentDetail
    form_class = StudentPaymentDetailForm
    template_name = 'students/studentpaymentdetail_form.html'
    redirect_field_name = 'students/paymentHistoryList_form.html'

    def get_form_kwargs(self):
        kwargs = super(StudentPaymentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self,form):
        form.instance.user = self.request.user
        student = form.cleaned_data.get('Student_Enrol_id')
        print("My student id is"+student)
        if Students.objects.filter(student_Id=student).filter(user=self.request.user).count() > 0:
            pass
        else:
            messages.error(self.request,"Student Id is not matching with our records, Please verify again")
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

class StudentPaymentDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'student_payment_details'
    login_url = 'login'
    model = StudentPaymentDetail
    template_name = 'students/payment_preview.html'

    def get_form_kwargs(self):
        kwargs = super(StudentPaymentDetailView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(StudentPaymentDetailView, self).get_context_data(**kwargs)
        fee_by = StudentPaymentDetail.objects.filter(pk=self.kwargs['pk']).all()
        # course = StudentPaymentDetail.objects.filter(pk=self.kwargs['pk'])
        print(fee_by[0])
        # if fee_by == "monthly_fee":
        #     context['actual_amount'] = Courses.objects.filter(name =course[0]).values_list('monthly_fee',flat=True)
        # elif fee_by == "yearly_fee":
        #     context['actual_amount'] = Courses.objects.filter(name=course[0]).values_list('yearly_fee', flat=True)
        # else:
        #     context['actual_amount'] = Courses.objects.filter(name=course[0]).values_list('quarterly_fee', flat=True)

        return context
    # def get_queryset(self):
    #         fee_by = StudentPaymentDetail.objects.filter(pk=self.kwargs['pk']).values_list('fee_by',flat=True)
    #         print(fee_by)
    #         return fee_by[0]

class StudentPaymentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    form_class = StudentPaymentDetailForm
    redirect_field_name = 'students/paymentHistoryList_form.html'
    model = StudentPaymentDetail
    # def form_valid(self,form):
    #     student = form.cleaned_data.get('Student_Enrol_id')
    #     try:
    #         student_name = Students.objects.get(student_Id=student).filter(user=self.request.user)
    #     except:
    #         messages.error(self.request,"Student Id is not matching with our records, Please verify again")
    #         return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super(StudentPaymentUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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


@login_required()
def search_student(request):
    queryset= Students.objects.filter(user = request.user)
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query)|
            Q(Student_Enrol_id__icontains=query)
            ).distinct()
    return render(request,'students/ajax_search.html',{'students':queryset})

@login_required()
def generate_payment_receipt(request,pk):
    student_detail = StudentPaymentDetail.objects.get(pk=pk)
    print(student_detail)
    total_paid_amount = StudentPaymentDetail.objects.filter(Student_Enrol_id=student_detail.Student_Enrol_id).aggregate(Sum('paid_amount')).get('paid_amount__sum',0.00)
    print(total_paid_amount)
    # total_paid_amount = StudentPaymentDetail.objects.filter(student=student[0]).aggregate(Sum('paid_amount'))
    actual_course_amount = Courses.objects.filter(name=student_detail.course_name).values_list('monthly_fee',flat=True)
    print("actual amount is below")
    print(actual_course_amount[0])
    dueAmount = actual_course_amount[0] - total_paid_amount

    html = render_to_string('students/pdf.html', {'student_detail':student_detail,'total_paid_amount':total_paid_amount,'due_amount':dueAmount})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="mypdf.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response


def display_pdf(request,pk):
    generate_payment_receipt(request,pk)
    # http://www.supinfo.com/articles/single/379-generate-pdf-files-out-of-html-templates-with-django
    # return  redirect('students:payment_preview', pk=pk)
#     Maybe you want to store the PDF file, we can do it using Django SimpleUploadedFiles. Let's say you have a field on your User model, called pdf_report (This snippet takes place after the pdf_file generation, before the HttpResponse creation) :
# from django.core.files.uploadedfile import SimpleUploadedFile
#
#     user.pdf_report = SimpleUploadedFile('Report-'+ user.first_name +'.pdf', pdf_file, content_type='application/pdf')
#     user.save()
# In order to not have to keep generating the PDF each time the user access the page, you will now store it in the database.
# I encourage you to try it if you have to automate receipts generation for orders, it does not take a lot of resources to generate a file, and depending on your template complexity, it's really fast.
    return '<a href="{}">PDF</a>'.format(reverse('students:payment_preview', args=pk))

class PendingStudentListView(LoginRequiredMixin,ListView):
    template_name ='students/pendingPaymentListView.html'
    model = SendNotification
    paginate_by = 15
    def get_queryset(self):
        return SendNotification.objects.filter(created_date__lte=timezone.now()).filter(user = self.request.user).order_by('-created_date')
