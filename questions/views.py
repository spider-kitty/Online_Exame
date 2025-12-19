
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Question

class QuestionListView(#LoginRequiredMixin,
 ListView):
    """View to list all questions"""
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'
    paginate_by = 10
    login_url = 'login'

    def get_queryset(self):
        return Question.objects.select_related('exam').order_by('-exam__created_at')

class QuestionDetailView(#LoginRequiredMixin,
 DetailView):
    """View to display a single question"""
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choices.all()
        return context

class QuestionCreateView(#LoginRequiredMixin, UserPassesTestMixin,
CreateView):
    """View to create a new question"""
    model = Question
    template_name = 'questions/question_form.html'
    fields = ['exam', 'question_type', 'text', 'marks', 'image']
    login_url = 'login'
    success_url = reverse_lazy('questions:question-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class QuestionUpdateView(#LoginRequiredMixin,UserPassesTestMixin,
 UpdateView):
    """View to update a question"""
    model = Question
    template_name = 'questions/question_form.html'
    fields = ['exam', 'question_type', 'text', 'marks', 'image']
    login_url = 'login'
    success_url = reverse_lazy('questions:question-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser
