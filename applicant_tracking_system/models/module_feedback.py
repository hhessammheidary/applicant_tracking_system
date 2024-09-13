from django.contrib.auth.models import User
from django.db import models
from .module_interview import Interview


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    text = models.TextField()
