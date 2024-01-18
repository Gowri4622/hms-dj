from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/announcements/', views.AnnouncementList.as_view()),
    path('api/announcement/<int:pk>/', views.AnnouncementDetail.as_view()),

    path('api/outpass-requests/', views.OutPassRequestList.as_view()),
    path('api/outpass-request/<int:pk>/', views.OutPassRequestDetail.as_view()),

    path('api/maintenance-requests/', views.MaintenanceRequestList.as_view()),
    path('api/maintenance-request/<int:pk>/', views.MaintenanceRequestDetail.as_view()),



]
