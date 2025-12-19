from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Grading

class GradingListView(#LoginRequiredMixin,UserPassesTestMixin,
 ListView):
    model = Grading
    template_name = 'grading/grading_list.html'
    context_object_name = 'gradings'
    paginate_by = 10
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        return Grading.objects.select_related('submission', 'graded_by').order_by('-graded_at')

class GradingDetailView(#LoginRequiredMixin,UserPassesTestMixin,
  DetailView):
    model = Grading
    template_name = 'grading/grading_detail.html'
    context_object_name = 'grading'
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class GradingUpdateView(#LoginRequiredMixin,UserPassesTestMixin,
 UpdateView):
    model = Grading
    template_name = 'grading/grading_form.html'
    fields = ['marks_awarded', 'feedback']
    login_url = 'login'
    success_url = reverse_lazy('grading:grading-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.graded_by = self.request.user
        return super().form_valid(form)
