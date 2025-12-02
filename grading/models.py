from django.db import models
from submissions.models import Submission
from django.conf import settings

class Grading(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name='grading')
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 'teacher'},
        related_name='gradings'
    )
    marks_awarded = models.DecimalField(max_digits=5, decimal_places=2)
    graded_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.submission.student.username} - {self.marks_awarded}"
