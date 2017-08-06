from django.conf.urls import url,include
from students import views

app_name = 'students'


urlpatterns =[
    url(r'^$',views.StudentsListView.as_view(),name='student_list'),
    url(r'^new/$', views.StudentsCreateView.as_view(), name='student_new'),
    url(r'^(?P<pk>\d+)/$',views.StudentsDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.StudentsUpdateView.as_view(), name='student_edit'),
    url(r'^course/',include('courses.urls',namespace='course')),
]
