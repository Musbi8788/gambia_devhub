from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, related_name="collaborations", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    video = models.FileField(upload_to="project_videos/", blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
