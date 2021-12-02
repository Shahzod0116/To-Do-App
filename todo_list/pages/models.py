from django.db import models
from django.urls import reverse


# Create your models here.
class Todo(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])