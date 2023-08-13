from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    photo = models.ImageField(max_length=255, null=True, blank=True, default="profile_images/d.png")


    def __str__(self):
        return self.name


class UserNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

