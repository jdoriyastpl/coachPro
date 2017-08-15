from django import forms
from students.models import Students,StudentPaymentDetail
from courses.models import Courses
from django.utils import timezone
from django.conf import settings

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','course_name','subject','remark','picture','age','father_name','address1','address2','city','state','adhaar_number']

    def __init__(self, user, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].queryset = Courses.objects.filter(user=user)

class StudentPaymentDetailForm(forms.ModelForm):
    actual_amount = forms.DecimalField(max_digits=20,decimal_places=2)

    class Meta:
        model = StudentPaymentDetail
        fields = ['student','course_name','paid_amount','fee_by','payment_date','next_payment_date']

    # # def __init__(self, *args, **kwargs):
    #         super(StudentPaymentDetailForm, self).__init__(*args, **kwargs)
    #         self.fields["payment_date"]= DateField(input_formats=settings.DATE_INPUT_FORMATS)
    #         self.fields["next_payment_date"]= DateField(input_formats=settings.DATE_INPUT_FORMATS)
