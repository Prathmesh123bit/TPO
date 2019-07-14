from django.conf.urls import include,url
from training_app import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
]
