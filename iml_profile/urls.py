from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.career_list, name='career_list'),
    path('award/', views.award_list, name='award_list'),
]