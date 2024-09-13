from django.db import models


class Applicant(models.Model):

    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('inProgress', 'inProgress'),
        ('accepted', 'accepted'),
        ('failed', 'failed'),
    )

    GENDER_CHOICES = (
        ('none', 'none'),
        ('male', 'male'),
        ('female', 'female'),
    )

    name = models.CharField(max_length=50)
    cv = models.TextField()
    linkedin = models.URLField()
    age = models.PositiveIntegerField()
    gender = models.TextField(choices=GENDER_CHOICES, default='n', max_length=6)
    status = models.TextField(choices=STATUS_CHOICES, default='p', max_length=10)

    def __str__(self):
        return self.name
