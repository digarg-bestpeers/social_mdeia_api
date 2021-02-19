from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

  class Meta:
    ordering = ['-id']

  def __str__(self):
    return self.body
