from django.contrib import admin
from students.models import Students,StudentPaymentDetail,SendNotification
# Register your models here.
admin.site.register(Students)
admin.site.register(SendNotification)
admin.site.register(StudentPaymentDetail)
