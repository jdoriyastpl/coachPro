"""coachPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from . import views
from adminPro.views import login_view as init_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.IndexView.as_view(),name='home'),
    url(r'^$', init_view ,name='login'),
    url(r'adminPro/',include('adminPro.urls',namespace='adminPro')),
    url(r'^student/',include('students.urls',namespace='student')),
    url(r'^course/',include('courses.urls',namespace='course')),
    url(r'adminPro/',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
