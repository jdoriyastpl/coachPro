from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
NAME_REGEX = '^[a-zA-Z]*$'
PHONE_REGEX ='^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False,
                                validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric or contain any of the following: ".+ -" ',
                                        code='invalid_username'
                                        )]
                                )
    first_name = models.CharField(max_length=255, blank=False,
                                  validators=[
                                        RegexValidator(
                                        regex = NAME_REGEX,
                                        message = 'Name must be Alphabetic',
                                        code='invalid_first_name'
                                        )]
                                )
    last_name = models.CharField(max_length=255, blank=False,
                                  validators=[
                                        RegexValidator(
                                        regex = NAME_REGEX,
                                        message = 'Name must be Alphabetic',
                                        code='invalid_last_name'
                                        )]
                                )
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    picture = models.ImageField(null=True,
                                blank=True,
                                default='img/default.png',
                                height_field="height_field",
                                width_field="width_field",
                                verbose_name="profile picture"
                                )
    institute_name = models.CharField(max_length=255,blank=False)
    address = models.CharField(max_length=255,blank=True)
    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)
    USERNAME_FIELD = 'email' # use email to log in
    REQUIRED_FIELDS = ['username'] # required when user is created

    def get_absolute_url(self):
        return reverse("adminPro:user_profile", kwargs={"username": self.username})
