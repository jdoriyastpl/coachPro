from django import forms
from courses.models import Courses


class CoursesForm(forms.ModelForm):

    class Meta:
        model = Courses
        fields =['name','monthly_fee','quarterly_fee','yearly_fee']


    def clean(self):
        cleaned_data = super(CoursesForm, self).clean()
        course_name = cleaned_data.get('name')

        if Courses.objects.filter(name=course_name).filter(self.request.user).count()>0 :
            raise forms.ValidationError('This Course is already added into system')
        return cleaned_data