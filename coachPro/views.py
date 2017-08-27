from django.views.generic import TemplateView
from students.models import Students,StudentPaymentDetail,SendNotification
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count,Sum
from rest_framework.permissions import IsAuthenticated

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


class ChartData(APIView,LoginRequiredMixin):
    authentication_classes = []
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.user)
        courses = Courses.objects.values_list('name',flat=True)
        # print(courses[0].)
        # print(len(courses))

        no_students = []
        for item in range(len(courses)):
            no_std = Courses.objects.filter(name=courses[item]).annotate(student_count=Count('student_course'))

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

class getRevenueData(APIView):
        authentication_classes = []
        permission_classes = [IsAuthenticated]

        def get(self, request, format=None):
            print(request.user)
            courses = Courses.objects.values_list('name',flat=True)

            total_revenue = []
            for item in range(len(courses)):
                paise = StudentPaymentDetail.objects.filter(course_name__name=courses[item]).aggregate(Sum('paid_amount')).get('paid_amount__sum',0.00)
                total_revenue.append(paise)

            # no_students = list(all_courses.course.all())
            course = list(courses)
            # print(no_students)

            data = {
                    "course": course,
                    "total_revenue": total_revenue,
            }
            return Response(data)
