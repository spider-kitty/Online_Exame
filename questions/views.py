from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Question, Choice


class QuestionListView(LoginRequiredMixin, ListView):
    """View to list all questions for an exam"""
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'
    paginate_by = 10
    login_url = 'login'

    def get_queryset(self):
        queryset = Question.objects.all()
        exam_id = self.kwargs.get('exam_id')
        if exam_id:
            queryset = queryset.filter(exam_id=exam_id)
        return queryset.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'exam_id' in self.kwargs:
            context['exam_id'] = self.kwargs['exam_id']
        return context


class QuestionDetailView(LoginRequiredMixin, DetailView):
    """View to display a single question with its choices"""
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['choices'] = question.choices.all()
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    """View to create a new question"""
    model = Question
    template_name = 'questions/question_form.html'
    fields = ['exam', 'question_type', 'text', 'marks', 'image']
    login_url = 'login'
    success_url = reverse_lazy('question-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Question'
        return context
