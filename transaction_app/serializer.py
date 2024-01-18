from rest_framework import serializers
from master_app.models import Student, Warden
from .models import OutPassRequest, Announcements, MaintenanceRequest
from django.contrib.auth import get_user_model


class OutPassRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutPassRequest
        fields = '__all__'


class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'
    

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

    
    


