from django.db import models
from datetime import datetime
from django.utils import timezone
from master_app.models import Warden,Student
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import timedelta


class Announcements(models.Model):
    warden_id = models.ForeignKey(Warden, on_delete=models.CASCADE, blank=True)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Announcement {self.pk}"


class OutPassRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, blank=True,null=True)
    warden = models.ForeignKey(Warden , on_delete = models.RESTRICT, blank=True,null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    total_days=models.IntegerField(blank=True)
    reason = models.TextField()
    rejected_reason=models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=10,default='pending',blank=True)

    def __str__(self):
        return f"Outpass request {self.pk}"

    def clean(self):
        if self.from_date > self.to_date:
            raise ValidationError("From date should be before or equal to to date")

    def save(self, *args, **kwargs):
        delta = self.to_date - self.from_date
        self.total_days = delta.days + 1  

        super().save(*args, **kwargs)
    

class MaintenanceRequest(models.Model):
    student = models.ForeignKey(Student , on_delete = models.RESTRICT,blank=True,null=True)
    warden = models.ForeignKey(Warden , on_delete = models.RESTRICT,blank=True,null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    request_reason = models.TextField()
    reply = models.TextField(default=False,blank=True,null=True)
    status = models.CharField(max_length=10, default='pending',blank=True,null=True)
