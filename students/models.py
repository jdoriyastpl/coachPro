from django.db import models
from django.utils import timezone
from datetime import datetime
import random as stdlib_random
import string
from django.core.urlresolvers import reverse
from courses.models import Courses
from django.core.validators import MaxValueValidator
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
User = settings.AUTH_USER_MODEL
d = datetime.today()
class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.ForeignKey(Courses,related_name="student_course")
    name = models.CharField(max_length=200)
    student_Id = models.CharField(max_length=200,default="STU"+str(d.year)+str(d.month)+''.join(stdlib_random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6)))
    created_date = models.DateTimeField(default=timezone.now)
    remark = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=150)
    age = models.PositiveIntegerField(null= False,verbose_name="Student Age")
    father_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=255,null=False)
    address2 = models.CharField(max_length=255,null=False)
    city = models.CharField(max_length=80,null=False)
    state = models.CharField(max_length=80,null=False)
    adhaar_number =models.CharField(max_length=255,null=False)
    picture = models.ImageField(null=True,
                                blank=True,
                                default='students/img/default.png',
                                height_field="height_field",
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)

    def get_absolute_url(self):
        return reverse("students:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class StudentPaymentDetail(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    FEE = (
        ('monthly_fee','Monthly'),
        ('quarterly_fee','Quarterly'),
        ('yearly_fee','YEARLY')
    )
    fee_by = models.CharField(max_length=15, choices=FEE,blank=True,verbose_name="Choose fee options",default=FEE[0][0])
    student = models.CharField(max_length=200,blank=True)
    Student_Enrol_id = models.CharField(max_length=200)
    course_name = models.ForeignKey(Courses,related_name='course_name')
    paid_amount = models.DecimalField(max_digits=20,decimal_places=2,null=False)
    payment_date = models.DateTimeField(default=timezone.now)
    next_payment_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Student_Enrol_id

    def get_absolute_url(self):
       return reverse("students:student_payment_history",kwargs={'Student_Enrol_id':self.Student_Enrol_id})

@receiver(post_save,sender=StudentPaymentDetail)
def update_student_name(sender,created,**kwargs):
    id = kwargs.get('instance')
    print("inside post_save signal"+str(id))
    student_name = Students.objects.values_list("name", flat=True).filter(student_Id=id)
    print(student_name[0])
    if created:
        StudentPaymentDetail.objects.filter(Student_Enrol_id=id).update(student=student_name[0])


class SendNotification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    student = models.ForeignKey(Students)
    is_payment_pending = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name
