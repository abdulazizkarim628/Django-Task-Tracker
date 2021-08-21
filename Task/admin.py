from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_created', 'expiry_date')


admin.site.register(Task, TaskAdmin)