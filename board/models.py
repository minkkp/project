from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)