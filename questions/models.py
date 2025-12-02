from django.db import models
from exams.models import Exam


class Question(models.Model):
    QUESTION_TYPES = (
        ('mcq', 'Multiple Choice'),
        ('short', 'Short Answer'),
        ('file', 'File Upload'),
    )

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    text = models.TextField()
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.text[:50]} ({self.get_question_type_display()})"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice for: {self.question.text[:30]}"
