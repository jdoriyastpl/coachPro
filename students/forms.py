from django import forms
from students.models import Students
from courses.models import Courses



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = {'name','course_name','subject','remark','age','father_name','address1','address2','city','state','adhaar_number'}
