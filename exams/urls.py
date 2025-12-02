from django.urls import path
from .views import ExamLoginView, ExamListView, ExamDetailView, ExamCreateView


app_name = 'exams'

urlpatterns = [
    path('login/', ExamLoginView.as_view(), name='login'),
    path('', ExamListView.as_view(), name='exam-list'),
    path('<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('create/', ExamCreateView.as_view(), name='exam-create'),

]

