from .models import CustomUser
from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.mixins import ListModelMixin
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import permissions
from rest_framework import generics

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            queryset = CustomUser.objects.all()
                
        else:
            return CustomUser.objects.filter(id=self.request.user.id)

        return queryset


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer