from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Exam
from django.contrib.auth.views import LoginView

class ExamLoginView(LoginView):
    template_name = 'exams/login.html'  
    success_url = '/exams/'


class ExamListView(LoginRequiredMixin, ListView):
    """View to list all exams"""
    model = Exam
    template_name = 'exams/exam_list.html'
    context_object_name = 'exams'
    paginate_by = 10
    login_url = 'login'
    
    def get_queryset(self):
        queryset = Exam.objects.filter(is_active=True)
        return queryset.order_by('-created_at')

class ExamDetailView(LoginRequiredMixin, DetailView):
    """View to display a single exam"""
    model = Exam
    template_name = 'exams/exam_detail.html'
    context_object_name = 'exam'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam = self.get_object()
        context['questions'] = exam.questions.all()
        return context

class ExamCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """View to create a new exam"""
    model = Exam
    template_name = 'exams/exam_form.html'
    fields = ['title', 'description', 'start_time', 'end_time', 'duration_minutes', 'total_marks', 'passing_marks']
    login_url = 'login'
    success_url = reverse_lazy('exam-list')
    
    def test_func(self):
        return self.request.user.role == 'teacher' if hasattr(self.request.user, 'role') else False
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
