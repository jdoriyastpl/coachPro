from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentPaymentDetail, SendNotification
from django.dispatch import Signal

# @receiver(post_save, sender=StudentPaymentDetail)
# def send_notification(sender,instance, **kwargs):
#     if kwargs.get('created', False):
#         notification = SendNotification.objects.create(student=instance,
#                                                       is_payment_pending=True)



# # In signals.py

pending_payment = Signal(providing_args=["student"])
#
#
