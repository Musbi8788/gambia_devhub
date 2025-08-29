from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)  # e.g. "Python, Django"
    level = models.CharField(max_length=20, choices=LEVELS, default='beginner')
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to="profile_images/", default="default.png")

    def __str__(self):
        return self.user.username
