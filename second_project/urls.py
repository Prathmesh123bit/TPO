"""second_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from placement_app import views
urlpatterns = [
    path('admin/', admin.site.urls),#path to which it will be directed mentioned in this path
    url(r'placement_app/',include('placement_app.urls')), #whatever we want to type on url to display typed it here
    url(r'job_app/',include('placement_app.urls')),
    url(r'Applicant_app/',include('placement_app.urls')),
    url(r'training_app/',include('placement_app.urls'))


]
