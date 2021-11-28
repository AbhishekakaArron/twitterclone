from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following' , on_delete=CASCADE)
    following = models.ForeignKey(User, related_name='followed_by', on_delete=CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)