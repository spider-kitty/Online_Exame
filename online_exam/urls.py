"""
URL configuration for online_exam project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # add this line
    path('exams/', include('exams.urls')),
    path('questions/', include('questions.urls')),
    path('submissions/', include('submissions.urls')),
    path('grading/', include('grading.urls')),
]
