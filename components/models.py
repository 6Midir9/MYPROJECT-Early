from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    price = models.CharField(max_length=255)
    contact_email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title