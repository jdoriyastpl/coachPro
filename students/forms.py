from django import forms
from students.models import Students,StudentPaymentDetail
from courses.models import Courses



class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','course_name','subject','remark','picture','age','father_name','address1','address2','city','state','adhaar_number']


class StudentPaymentDetailForm(forms.ModelForm):
    actual_amount = forms.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        model = StudentPaymentDetail
        fields = ['student','course_name','paid_amount','payment_date']
