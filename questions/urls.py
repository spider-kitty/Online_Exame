from django.urls import path
from .views import QuestionListView, QuestionDetailView, QuestionCreateView

app_name = 'questions'

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('create/', QuestionCreateView.as_view(), name='question-create'),
]
