from students.models import Students,StudentPaymentDetail,SendNotification
from django.utils import timezone
from datetime import datetime
from students.signals import pending_payment
from django.db.models import Sum
from courses.models import Courses

def pending_payment_count(request):
    if request.user.is_authenticated:
        user = request.user
        students_Id = StudentPaymentDetail.objects.values_list("Student_Enrol_id", flat=True).distinct()
        print(students_Id)
        for student_id in students_Id:
            student = Students.objects.filter(student_Id=student_id)
            if student.exists():
                print(student[0])
                last_expected_payment_dates = StudentPaymentDetail.objects.values_list("next_payment_date", flat=True).filter(student=student[0]).order_by("-pk")
                # student_detail = StudentPaymentDetail.objects.get(student=student[0])
                print("ffsdfgddgdf")
                # print(student_detail)
                total_paid_amount = StudentPaymentDetail.objects.filter(student=student[0]).aggregate(Sum('paid_amount')).get('paid_amount__sum',0.00)
                actual_course_amount = Courses.objects.filter(name=student[0].course_name).values_list('monthly_fee',flat=True)
                course =student[0].course_name
                print(course)
                due_amount = actual_course_amount[0] - total_paid_amount
                print(len(last_expected_payment_dates))
                print(last_expected_payment_dates)
                if len(last_expected_payment_dates)==0:
                    pass
                elif len(last_expected_payment_dates)>1:
                    last_expected_payment_date = last_expected_payment_dates[1]
                    if datetime.now() >=last_expected_payment_date:
                        print("Student Payment is pending")
                        try:
                            SendNotification.objects.get(student=student[0])
                        except SendNotification.DoesNotExist:
                            pending_payment.send(sender=StudentPaymentDetail,student=student[0],user=user,due_amount=due_amount,due_amount_date=last_expected_payment_date)
                            Pending_students = SendNotification.objects.filter(is_payment_pending=True).count()
                            return {'Pending_students': Pending_students}
        # not_viewed = SendNotification.objects.filter(user=user, viewed=False).count()
        # Pending_students = SendNotification.objects.filter(is_payment_pending=True).count()


    return {}
