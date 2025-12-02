from django.contrib import admin
from .models import Grading

@admin.register(Grading)
class GradingAdmin(admin.ModelAdmin):
    list_display = ('submission', 'graded_by', 'marks_awarded', 'graded_at')
    search_fields = ('submission__student__username', 'submission__question__text')
