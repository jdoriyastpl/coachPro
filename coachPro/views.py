from django.views.generic import TemplateView
from students.models import Students,StudentPaymentDetail,SendNotification
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,TemplateView):
    login_url = 'login'
    template_name ='dashboard.html'

    def get_context_data(self,*args, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Enrolled_students'] = Students.objects.filter(user=self.request.user).count()
        context['Pending_students'] = SendNotification.objects.filter(is_payment_pending=True).count()
        return context
