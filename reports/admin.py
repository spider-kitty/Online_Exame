from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'total_score', 'percentage', 'passed')
    list_filter = ('exam', 'passed')
    search_fields = ('student__username', 'exam__title')
