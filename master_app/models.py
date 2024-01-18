from django.db import models
from multiselectfield import MultiSelectField

ROOM_ASSETS_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('Water Heater', 'Water Heater'),
        ('Fridge', 'Fridge'),
        ('Stove', 'Stove'),
    ]

ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Two share', 'Two share'),
        ('Three share', 'Three share'),
        ('Four share', 'Four share'),
    ]


class Hostel(models.Model):
    HOSTEL_TYPES = [
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        
    ]

    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        
    ]
    

    hostel_name = models.CharField(max_length=255)
    hostel_type = models.CharField(max_length=10, choices=HOSTEL_TYPES)
    location = models.CharField(max_length=255)
    number_of_floors = models.PositiveIntegerField()
    number_of_rooms = models.PositiveIntegerField()
    warden_assigned = models.CharField(max_length=255)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='hostels')

    def __str__(self):
        return self.hostel_name


    



class Warden(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    register_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    qualification = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    hostel = models.ForeignKey(Hostel, on_delete=models.RESTRICT, related_name='warden')
    hostel_assigned = models.CharField(max_length=100, default="Hostel_Name")
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wardens')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    register_number = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    parents_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)
    department = models.CharField(max_length=50)
    check_in_date = models.DateField()
    hostel = models.ForeignKey(Hostel, on_delete=models.RESTRICT, related_name='hostelstudent')
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='students')
   

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Room(models.Model):
    ROOM_ASSETS_CHOICES = [
        ('Air Conditioner', 'Air Conditioner'),
        ('Water Heater', 'Water Heater'),
        ('Fridge', 'Fridge'),
        ('Stove', 'Stove'),
    ]

    ROOM_TYPE_CHOICES = [
        ('Single', ''),
        ('Two share', 'Water Heater'),
        ('Three share', 'Fridge'),
        ('Four share', 'Stove'),
    ]

    student = models.ForeignKey(Student, on_delete=models.RESTRICT,blank=True,null=True)
    room_number = models.CharField(max_length=5)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    room_assets = models.CharField(choices=ROOM_ASSETS_CHOICES,max_length=100)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f"{self.room_number}"
    



class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    child = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class HostelFees(models.Model):
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    transport = models.DecimalField(max_digits=10, decimal_places=2)
    hostel = models.ForeignKey(Hostel, on_delete=models.RESTRICT)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fees')

    def __str__(self):
        return {self.hostel}


