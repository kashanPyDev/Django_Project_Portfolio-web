from django.db import models


# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Message = models.TextField()
