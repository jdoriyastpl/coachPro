# In receivers.py
from django.dispatch import receiver
from .signals import *
from students.models import StudentPaymentDetail,Students

@receiver(pending_payment)
def create_pending_payment_record(sender, **kwargs):
    student = kwargs['student']
    notification = SendNotification.objects.create(student=student,
                                                  is_payment_pending=True)
