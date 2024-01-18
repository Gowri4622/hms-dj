from django.contrib import admin


from .models import Announcements,OutPassRequest,MaintenanceRequest


admin.site.register(Announcements)
admin.site.register(OutPassRequest)
admin.site.register(MaintenanceRequest)