
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Submission

class SubmissionListView(#LoginRequiredMixin,
 ListView):
    model = Submission
    template_name = 'submissions/submission_list.html'
    context_object_name = 'submissions'
    paginate_by = 10
    login_url = 'login'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Submission.objects.select_related('exam', 'student').order_by('-submitted_at')
        return Submission.objects.filter(student=self.request.user).order_by('-submitted_at')

class SubmissionDetailView(#LoginRequiredMixin,
 DetailView):
    model = Submission
    template_name = 'submissions/submission_detail.html'
    context_object_name = 'submission'
    login_url = 'login'

class SubmissionCreateView(#LoginRequiredMixin,
 CreateView):
    model = Submission
    template_name = 'submissions/submission_form.html'
    fields = ['exam', 'answers']
    login_url = 'login'
    success_url = reverse_lazy('submissions:submission-list')

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class SubmissionUpdateView(#LoginRequiredMixin,
 UpdateView):
    model = Submission
    template_name = 'submissions/submission_form.html'
    fields = ['answers']
    login_url = 'login'
    success_url = reverse_lazy('submissions:submission-list')
