from .models import Student,HostelFees,Hostel,Parent,Warden,Room
from django.shortcuts import render
from .serializer import StudentSerializer,HostelFeesSerializer,HostelSerializer,ParentSerializer,WardenSerializer,RoomSerializer
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
	

# Student views
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user

        # Check if the user is a warden
        if user.is_staff or user.user_role == 'Warden':
            queryset = Student.objects.all()
                
        else:
            # Assuming register_number is the field you want to filter on
            queryset = Student.objects.filter(register_number=user.username)

        return queryset



class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()



#Hostel Views
class HostelList(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save()


class HostelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


#Rooms View
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        latest_student = Student.objects.latest('id')

# Now you can access the 'student_id' of the latest student
        latest_student_id = latest_student.id
        serializer.save(student=latest_student)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


#Warden views
class WardenList(generics.ListCreateAPIView):
    # queryset=Warden.objects.all()
    serializer_class = WardenSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Warden.objects.all()
        else:
            # Assuming register_number is the field you want to filter on
            queryset = Warden.objects.filter(register_number=user.username)

        return queryset


    def perform_create(self, serializer):
        # Assuming you want to handle the case of multiple hostels by choosing the first one
        hostels = Hostel.objects.filter()
        
        if hostels.exists():
            hostel_instance = hostels.first()
            serializer.save(hostel=hostel_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Handle the case where no hostel is found or multiple hostels are found
            return Response({'error': 'No hostel found or multiple hostels found'}, status=status.HTTP_400_BAD_REQUEST)


class WardenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warden.objects.all()
    serializer_class = WardenSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


#Parents View
class ParentList(generics.ListCreateAPIView):
    # queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = Parent.objects.all()
        else:
            # Assuming register_number is the field you want to filter on
            queryset = Parent.objects.filter(child=user.username)

        return queryset
    
    def perform_create(self, serializer):
        latest_student = Student.objects.latest('id')

# Now you can access the 'student_id' of the latest student
        latest_student_id = latest_student.id
        serializer.save(child=latest_student)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)



#Hostel Views
class HostelFeeList(generics.ListCreateAPIView):
    queryset = HostelFees.objects.all()
    serializer_class = HostelFeesSerializer
    permission_classes = [permissions.IsAuthenticated]  

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class HostelFeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HostelFees.objects.all()
    serializer_class = HostelFeesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_update(self, serializer):
    #     serializer.save(owner=self.request.user)