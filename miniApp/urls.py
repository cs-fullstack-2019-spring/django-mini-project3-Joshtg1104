from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registry/', views.timecard, name='registry'),
    path('registry/edit/<int:id>/', views.edit, name='edit'),
]
