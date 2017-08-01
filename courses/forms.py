from django import forms
from courses.models import Courses


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields ={'name','monthly_fee','quarterly_fee','yearly_fee'}
