from django import forms
from students.models import Students,StudentPaymentDetail
from courses.models import Courses
from django.utils import timezone
from django.conf import settings
from datetimewidget.widgets import DateTimeWidget
dateTimeOptions = {
'format': 'dd/mm/yyyy HH:ii P',
'autoclose': True,
'showMeridian' : True
}
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','course_name','subject','phone_number','picture','age','father_name','address1','address2','city','state','adhaar_number']

    def __init__(self, user, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].queryset = Courses.objects.filter(user=user)

    # def clean(self):
    #     cleaned_data = super(StudentForm, self).clean()
    #     student_name = cleaned_data.get('name')
    #
    #     if Students.objects.filter(name=student_name).filter(self.request.user).count() > 0:
    #         raise forms.ValidationError('This Student is already added into system')
    #     return cleaned_data

class StudentPaymentDetailForm(forms.ModelForm):
    # actual_amount = forms.DecimalField(max_digits=20,decimal_places=2)

    class Meta:
        model = StudentPaymentDetail
        fields = ['Student_Enrol_id','course_name','paid_amount','fee_by','payment_date','next_payment_date']

        # widgets = {
        #     'payment_date': forms.DateInput(attrs={'class':'datepicker'}),
        #     'next_payment_date': forms.DateInput(attrs={'class':'datepicker'}),
        # }
    def __init__(self, user, *args, **kwargs):
        super(StudentPaymentDetailForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].queryset = Courses.objects.filter(user=user)
    # # def __init__(self, *args, **kwargs):
    #         super(StudentPaymentDetailForm, self).__init__(*args, **kwargs)
    #         self.fields["payment_date"]= DateField(input_formats=settings.DATE_INPUT_FORMATS)
    #         self.fields["next_payment_date"]= DateField(input_formats=settings.DATE_INPUT_FORMATS)
