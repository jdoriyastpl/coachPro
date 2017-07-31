from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from adminPro import views

app_name = 'adminPro'

urlpatterns =[
    url(r'login/$',auth_view.LoginView.as_view(template_name='adminPro/login.html'),name='login'),
    url(r'logout/$',auth_view.logout,name='logout',kwargs={'next_page': '/'}),
    url(r'signup/$',views.UserFormView.as_view(),name='signup'),
]
