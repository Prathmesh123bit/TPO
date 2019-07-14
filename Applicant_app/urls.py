from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^Applicant_app$', views.index),
 ]
