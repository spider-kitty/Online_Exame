from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Grading

class GradingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """View to list all gradings for teachers only"""
    model = Grading
    template_name = 'grading/grading_list.html'
    context_object_name = 'gradings'
    paginate_by = 10
    login_url = 'login'
    
    def test_func(self):
        return hasattr(self.request.user, 'role') and self.request.user.role == 'teacher'

class GradingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """View to display a single grading"""
    model = Grading
    template_name = 'grading/grading_detail.html'
    context_object_name = 'grading'
    login_url = 'login'
    
    def test_func(self):
        return hasattr(self.request.user, 'role') and self.request.user.role == 'teacher'

class GradingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to update grading and provide feedback"""
    model = Grading
    template_name = 'grading/grading_form.html'
    fields = ['marks_awarded', 'feedback']
    login_url = 'login'
    success_url = reverse_lazy('grading-list')
    
    def test_func(self):
        return hasattr(self.request.user, 'role') and self.request.user.role == 'teacher'
    
    def form_valid(self, form):
        form.instance.graded_by = self.request.user
        return super().form_valid(form)
