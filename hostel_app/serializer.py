from rest_framework import serializers
from .models import CustomUser
# from master_app.serializer import StudentSerializer, WardenSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'user_role','user_student','user_warden','user_parent']



