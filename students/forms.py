from django import forms
from students.models import Students
from courses.models import Courses



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = {'name','course_name','subject','remark'}
