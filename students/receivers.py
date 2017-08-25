# In receivers.py
from django.dispatch import receiver
from .signals import *
from students.models import StudentPaymentDetail,Students

@receiver(pending_payment)
def create_pending_payment_record(sender, **kwargs):
    student = kwargs['student']
    user= kwargs["user"]
    due_amount = kwargs["due_amount"]
    next_payment_date = kwargs['due_amount_date']
    # course = kwargs['course']
    notification = SendNotification.objects.create(student=student,user=user,due_amount=due_amount,next_payment_date=next_payment_date,
                                                  is_payment_pending=True)
