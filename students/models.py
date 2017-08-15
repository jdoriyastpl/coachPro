from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from courses.models import Courses
from django.core.validators import MaxValueValidator
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.ForeignKey(Courses,related_name="student_course")
    name = models.CharField(max_length=200)
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
    fee_by = models.CharField(max_length=15, choices=FEE,blank=True)
    student = models.ForeignKey(Students,related_name='student_name')
    course_name = models.ForeignKey(Courses,related_name='course_name')
    paid_amount = models.DecimalField(max_digits=20,decimal_places=2,null=False)
    payment_date = models.DateTimeField(default=timezone.now)
    next_payment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.student.name

    def get_absolute_url(self):
       return reverse("students:student_payment_history",kwargs={'student':self.student.name})


class SendNotification(models.Model):
    student = models.ForeignKey(Students)
    is_payment_pending = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name
