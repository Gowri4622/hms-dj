from django.contrib.auth.models import AbstractUser
from django.db import models
from master_app.models import Student,Warden,Parent

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Warden', 'Warden'),
        ('Student', 'Student'),
        ('Parent','Parent')
    ]
    user_role = models.CharField(max_length = 10, choices=ROLE_CHOICES)
    user_student = models.OneToOneField(
        Student,
        on_delete=models.RESTRICT,
        related_name='student',
        null=True,
        blank=True,
    )
    user_warden = models.OneToOneField(
        Warden,
        on_delete=models.RESTRICT,
        related_name='warden',
        null=True,
        blank=True,
    )
    user_parent = models.OneToOneField(
        Parent,
        on_delete=models.RESTRICT,
        related_name='parent',
        null=True,
        blank=True,
    )
