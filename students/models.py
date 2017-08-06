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

    def get_absolute_url(self):
        return reverse("students:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name


class StudentFee(models.Model):
    student = models.ForeignKey(Students,related_name='student_name')
