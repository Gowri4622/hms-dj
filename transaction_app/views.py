from master_app.models import Student,Warden
from django.shortcuts import render
from .serializer import OutPassRequestSerializer,AnnouncementsSerializer,MaintenanceRequestSerializer
from .models import OutPassRequest,Announcements,MaintenanceRequest
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.mixins import ListModelMixin
from django.http import HttpResponse
from django.http import Http404
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.utils import timezone
	

# Student views
class AnnouncementList(generics.ListCreateAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [permissions.IsAuthenticated]  

    # def get_queryset(self):
    #     user = self.request.user

    #     # Check if the user is a warden
    #     if user.is_staff or user.user_role == 'Warden':
    #         queryset = Student.objects.all()
                
    #     else:
    #         # Assuming register_number is the field you want to filter on
    #         queryset = Student.objects.filter(register_number=user.username)

    #     return queryset
    def perform_create(self, serializer):
        user=self.request.user
        
        serializer.save(warden_id=user.user_warden)



class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()



#Hostel Views
class OutPassRequestList(generics.ListCreateAPIView):
    queryset = OutPassRequest.objects.all()
    serializer_class = OutPassRequestSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        user=self.request.user
        
        serializer.save(student=user.user_student)


class OutPassRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutPassRequest.objects.all()
    serializer_class = OutPassRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        user=self.request.user
        
        serializer.save(warden=user.user_warden)


#Rooms View
class MaintenanceRequestList(generics.ListCreateAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(student=user.user_student)


class MaintenanceRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        user=self.request.user
        serializer.save(warden=user.user_warden)


