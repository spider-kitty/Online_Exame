from django.urls import path
from .views import SubmissionListView, SubmissionDetailView, SubmissionCreateView, SubmissionUpdateView

app_name = 'submissions'

urlpatterns = [
    path('', SubmissionListView.as_view(), name='submission-list'),
    path('<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('create/', SubmissionCreateView.as_view(), name='submission-create'),
    path('<int:pk>/update/', SubmissionUpdateView.as_view(), name='submission-update'),
]
