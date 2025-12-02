from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'start_time', 'end_time', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
