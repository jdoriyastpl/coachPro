from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from adminPro import views

app_name = 'adminPro'

urlpatterns =[
    url(r'^profile/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^profile/(?P<username>\w+)/edit/$', views.user_profile_update, name='user_profile_update'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
