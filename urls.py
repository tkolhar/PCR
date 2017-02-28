"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from PCR import views

urlpatterns = [
    url(r'^PCR/', include('PCR.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^PCR/login/', views.get_name, name='get_name'),
    url(r'^PCR/patientaccesscenter/', views.patient_access_center,name='patient_access_center'),
    url(r'^PCR/search/', views.search,name='search'),
    url(r'^PCR/past_history/', views.search_history, name='search_history'),
    url(r'^PCR/logout/', views.logout, name='logout'),
    url(r'^PCR/add/', views.add, name='add'),
    url(r'^admin/', admin.site.urls),
]
