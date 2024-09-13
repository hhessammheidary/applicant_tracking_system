from django.contrib.auth.models import User
from django.db import models


class Interview(models.Model):

    TYPES_CHOICES = (
        ('phone', 'phone'),
        ('technical', 'technical'),
        ('code', 'code'),
        ('final', 'final'),
    )

    interviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(choices=TYPES_CHOICES, default='p', max_length=9)

