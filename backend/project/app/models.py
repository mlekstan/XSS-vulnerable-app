from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    date = models.DateTimeField(blank=True, null=True)