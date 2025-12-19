from django.urls import path
from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView

app_name = 'questions'

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('create/', QuestionCreateView.as_view(), name='question-create'),
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
]
