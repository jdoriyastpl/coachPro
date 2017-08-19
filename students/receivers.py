# In receivers.py
from django.dispatch import receiver
from .signals import *
from students.models import StudentPaymentDetail,Students

@receiver(pending_payment)
def create_pending_payment_record(sender, **kwargs):
    student = kwargs['student']
    user= kwargs["user"]
    notification = SendNotification.objects.create(student=student,user=user,
                                                  is_payment_pending=True)
