from django.db import models



class Name(models.Model):
    room = models.CharField(max_length=10)
    username = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room}-{self.username}"
# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(Name, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low'
    )




