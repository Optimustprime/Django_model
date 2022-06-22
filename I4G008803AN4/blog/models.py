from django.db import models
from django.conf import settings
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_Date=models.DateTimeField(auto_now_add=True)
    published_Date=models.DateTimeField(auto_now_add=True)
