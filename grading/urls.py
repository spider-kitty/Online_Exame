from django.urls import path
from .views import GradingListView, GradingDetailView, GradingUpdateView

app_name = 'grading'

urlpatterns = [
    path('', GradingListView.as_view(), name='grading-list'),
    path('<int:pk>/', GradingDetailView.as_view(), name='grading-detail'),
    path('<int:pk>/update/', GradingUpdateView.as_view(), name='grading-update'),
]
