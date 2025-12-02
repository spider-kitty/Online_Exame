from django.db import models
from exams.models import Exam
from django.contrib.auth.models import User


class Report(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='reports')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.exam.title}: {self.percentage}%"
