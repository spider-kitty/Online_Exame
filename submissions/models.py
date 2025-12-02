from django.db import models
from django.conf import settings
from exams.models import Exam
from questions.models import Question

class Submission(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='submissions'
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='submissions')
    text_answer = models.TextField(blank=True, null=True)
    file_answer = models.FileField(upload_to='submission_files/', blank=True, null=True)
    marks_awarded = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.exam.title} - {self.question.text[:30]}"
