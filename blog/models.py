from django.db import models
from django.conf import settings
from django.utils import timezone


class Board(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    body = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.title[:20]
