from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.career_list, name='career_list'),
    path('contact/', views.contact_me, name='contact_me'),
]