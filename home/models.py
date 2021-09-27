from django.db import models

# Create your models here.
class addTodo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now=True)
