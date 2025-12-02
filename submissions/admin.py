from django.contrib import admin
from .models import Submission

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'question', 'marks_awarded', 'submitted_at')
    list_filter = ('exam', 'submitted_at')
    search_fields = ('student__username', 'question__text')
