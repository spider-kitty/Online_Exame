from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Submission

class SubmissionListView(LoginRequiredMixin, ListView):
    """View to list all submissions for a student or teacher"""
    model = Submission
    template_name = 'submissions/submission_list.html'
    context_object_name = 'submissions'
    paginate_by = 10
    login_url = 'login'
    
    def get_queryset(self):
        if hasattr(self.request.user, 'role') and self.request.user.role == 'teacher':
            return Submission.objects.all()
        return Submission.objects.filter(student=self.request.user)

class SubmissionDetailView(LoginRequiredMixin, DetailView):
    """View to display a single submission"""
    model = Submission
    template_name = 'submissions/submission_detail.html'
    context_object_name = 'submission'
    login_url = 'login'
    
    def get_queryset(self):
        queryset = Submission.objects.all()
        if not (hasattr(self.request.user, 'role') and self.request.user.role == 'teacher'):
            queryset = queryset.filter(student=self.request.user)
        return queryset

class SubmissionCreateView(LoginRequiredMixin, CreateView):
    """View to create a new submission"""
    model = Submission
    template_name = 'submissions/submission_form.html'
    fields = ['exam', 'question', 'text_answer', 'file_answer']
    login_url = 'login'
    success_url = reverse_lazy('submission-list')
    
    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
