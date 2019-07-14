from django.conf.urls import include,url
from placement_app import views

urlpatterns = [

    url(r'^$',views.index,name='index'),
]
