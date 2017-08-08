from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from courses.models import Courses
from django.core.validators import MaxValueValidator
# Create your models here.

class Students(models.Model):
    course_name = models.ManyToManyField(Courses,related_name="student_course")
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
    adhaar_number =models.PositiveIntegerField()
    picture = models.ImageField(null=True,
                                blank=True,
                                default='/students/img/default.png',
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
    student = models.OneToOneField(Students,related_name='student_name')
    course_name = models.ForeignKey(Courses,related_name='course_name')
    paid_amount = models.DecimalField(max_digits=20,decimal_places=2,null=False)
    payment_date = models.DateTimeField(default=timezone.now)
