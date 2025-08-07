from django.db import models

# Create your models here.
class Task(models.Model):
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

