from django.conf.urls import url,include
from students import views

app_name = 'students'


urlpatterns =[
    url(r'^$',views.StudentsListView.as_view(),name='student_list'),
    url(r'^new/$', views.StudentsCreateView.as_view(), name='student_new'),
    url(r'^search/$',views.search_student,name='student_search_result'),
    url(r'^(?P<pk>\d+)/$',views.StudentsDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.StudentsUpdateView.as_view(), name='student_edit'),
    url(r'^(?P<pk>\d+)/remove/$', views.StudentDeleteView.as_view(), name='student_remove'),
    url(r'^payment/$',views.StudentPaymentCreateView.as_view(),name='student_payment'),
    url(r'^payment/preview/(?P<pk>\d+)/$',views.StudentPaymentDetailView.as_view(),name='payment_preview'),
    url(r'^payment/preview/(?P<pk>\d+)/edit/$',views.StudentPaymentUpdateView.as_view(),name='payment_update'),
    url(r'^payment/history/(?P<Student_Enrol_id>.+?)/$', views.StudentPaymentHistoryListView.as_view(),name='student_payment_history'),
    # url(r'^history/(?P<student>\w+)$', views.StudentPaymentHistoryListView.as_view(),name='student_payment_history'),
    url(r'^course/',include('courses.urls',namespace='course')),
]
