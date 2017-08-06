from django.conf.urls import url
from courses import views

app_name = 'courses'


urlpatterns =[
    url(r'^$',views.CoursesListView.as_view(),name='course_list'),
    url(r'^new/$', views.CoursesCreateView.as_view(), name='course_new'),
    url(r'^(?P<pk>\d+)/$',views.CoursesDetailView.as_view(),name='course_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.CoursesUpdateView.as_view(), name='course_edit'),
]
