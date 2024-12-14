from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    "user" = models.ForeignKey(User, on_delete=models.CASCADE)
    "title" = models.CharField(max_length=60)
    "content" = models.TextField()
    "date" = models.DateTimeField()