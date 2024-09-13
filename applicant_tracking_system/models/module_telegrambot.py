from django.db import models
from .module_interview import Interview


class TelegramBot(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
