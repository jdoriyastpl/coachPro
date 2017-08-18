from students.models import Students,StudentPaymentDetail,SendNotification
from django.utils import timezone
from datetime import datetime
from students.signals import pending_payment


def pending_payment_count(request):
    if request.user.is_authenticated:
        user = request.user
        students = StudentPaymentDetail.objects.values_list("student", flat=True).distinct()
        for student_id in students:
            student = Students.objects.filter(pk=student_id)
            print(student[0])
            last_expected_payment_dates = StudentPaymentDetail.objects.values_list("next_payment_date", flat=True).filter(student=student[0]).order_by("-pk")
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
                        pending_payment.send(sender=StudentPaymentDetail,student=student[0])
                        Pending_students = SendNotification.objects.filter(is_payment_pending=True).count()
                        return {'Pending_students': Pending_students}
        # not_viewed = SendNotification.objects.filter(user=user, viewed=False).count()
        # Pending_students = SendNotification.objects.filter(is_payment_pending=True).count()


    return {}
