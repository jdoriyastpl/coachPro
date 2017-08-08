from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    monthly_fee = models.DecimalField(max_digits=20,decimal_places=2,blank=False)
    quarterly_fee = models.DecimalField(max_digits=20,decimal_places=2,blank=False)
    yearly_fee = models.DecimalField(max_digits=20,decimal_places=2,blank=False)

    def get_absolute_url(self):
        return reverse("courses:course_detail",kwargs={'pk':self.pk})

    def __unicode__(self):
        return self.name

    def __str__(self):       # if python 3
        return self.name
