from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('show_data', views.show_data , name='show_data'),


]