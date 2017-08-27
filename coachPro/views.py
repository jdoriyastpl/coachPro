from django.views.generic import TemplateView
from students.models import Students,StudentPaymentDetail,SendNotification
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count,Sum
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class IndexView(LoginRequiredMixin,TemplateView):
    login_url = 'login'
    template_name ='dashboard.html'

    def get_context_data(self,*args, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Enrolled_students'] = Students.objects.filter(user=self.request.user).count()
        context['Pending_students'] = SendNotification.objects.filter(is_payment_pending=True).filter(user=self.request.user).count()
        return context

@permission_classes((IsAuthenticatedOrReadOnly, ))
class ChartData(APIView,LoginRequiredMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        print("user name is ;;;;")
        print(self.request.user)
        courses = Courses.objects.values_list('name',flat=True).filter(user= request.user)
        # print(courses[0].)
        # print(len(courses))

        no_students = []
        for item in range(len(courses)):
            no_std = Courses.objects.filter(name=courses[item]).filter(user= request.user).annotate(student_count=Count('student_course'))

            print(no_std[0].student_count)
            no_students.append(no_std[0].student_count)

        # no_students = list(all_courses.course.all())
        course = list(courses)
        # print(no_students)

        data = {
                "course": course,
                "no_students": no_students,
        }
        return Response(data)
@permission_classes((IsAuthenticatedOrReadOnly, ))
class getRevenueData(APIView):
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

        def get(self, request, format=None):
            print(request.user)
            courses = Courses.objects.values_list('name',flat=True).filter(user= request.user)

            total_revenue = []
            for item in range(len(courses)):
                paise = StudentPaymentDetail.objects.filter(user= request.user).filter(course_name__name=courses[item]).aggregate(Sum('paid_amount')).get('paid_amount__sum',0.00)
                total_revenue.append(paise)

            # no_students = list(all_courses.course.all())
            course = list(courses)
            # print(no_students)

            data = {
                    "course": course,
                    "total_revenue": total_revenue,
            }
            return Response(data)
