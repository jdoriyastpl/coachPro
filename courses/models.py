from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL
class Courses(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    monthly_fee = models.DecimalField(max_digits=20,decimal_places=2)
    quarterly_fee = models.DecimalField(max_digits=20,decimal_places=2)
    yearly_fee = models.DecimalField(max_digits=20,decimal_places=2)

    def get_absolute_url(self):
        return reverse("courses:course_detail",kwargs={'pk':self.pk})

    def __unicode__(self):
        return self.name

    def __str__(self):       # if python 3
        return self.name
