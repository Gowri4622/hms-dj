from rest_framework import serializers
from .models import Student, Hostel, Room, Warden, Parent, HostelFees
from django.contrib.auth import get_user_model
import string
import random
from django.conf import settings



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'register_number', 'gender', 'date_of_birth', 'contact_number',
                  'email', 'parents_number', 'blood_group', 'department', 'check_in_date', 'hostel']

    def create(self, validated_data):
        register_number = validated_data['register_number']
        username = register_number

        def generate_password():
            length = 8
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(characters) for i in range(length))

        password = generate_password()

        user_data = {
            'username': username,
            'password': password,
            'user_role': 'Student',
        }

        print(username)
        print(password)
        user = get_user_model().objects.create(**user_data)

        user.set_password(password)
        user.save()

        
        student = Student.objects.create(**validated_data)
        user.user_student = student
        user.save()

        return student
    


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['hostel_name', 'hostel_type', 'location', 'number_of_floors', 'number_of_rooms', 'type_of_room', 'warden_assigned']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['student','room_number', 'room_type', 'room_assets']


class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = ['id','register_number','first_name', 'last_name', 'gender', 'date_of_birth', 'qualification', 'contact_number', 'email','hostel']

    def create(self, validated_data):
        first_name = validated_data['register_number']
        username = first_name.lower()

        def generate_password():
            length = 8
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(characters) for i in range(length))
        
        password = generate_password()

        user_data = {
            'username': username,
            'password': password,
            'user_role': 'Warden',  
        }

        print(username)
        print(password)
        user = get_user_model().objects.create(**user_data)

        user.set_password(password)
        user.save()

        
        warden = Warden.objects.create(**validated_data)
        user.user_warden = warden
        user.save()

        return warden



class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'student_name', 'contact_number', 'email','child']
    
    def create(self, validated_data):
        first_name = validated_data['first_name']
        username = first_name.lower()
        

        def generate_password():
            length = 8
            characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(characters) for i in range(length))
        
        password = generate_password()

        user_data = {
            'username': username,
            'password': password,
            'user_role': 'Parent',  
        }

        print(username)
        print(password)
        user = get_user_model().objects.create(**user_data)

        user.set_password(password)
        user.save()

        
        parent = Parent.objects.create(**validated_data)
        user.user_parent = parent
        user.save()

        return parent


class HostelFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelFees
        fields = ['rent', 'food', 'transport']



