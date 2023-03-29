from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images')
    created_on = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_user_id = models.PositiveSmallIntegerField()

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_comment = models.CharField(max_length=400)
    post_user_id = models.PositiveSmallIntegerField()