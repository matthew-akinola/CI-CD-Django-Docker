from django.db import models

# Create your models here.

class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, unique=True)
    file = models.FileField(null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ['-created_at']