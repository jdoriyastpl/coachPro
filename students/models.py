from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from courses.models import Courses
# Create your models here.

class Students(models.Model):
    course_name = models.ManyToManyField(Courses,related_name="student_course")
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    remark = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse("students:detail",kwargs={'pk':self.pk})
