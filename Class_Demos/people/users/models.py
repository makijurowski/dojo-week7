# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    friends = models.ManyToManyField('self', through='Friendships', symmetrical=False, related_name='my_friends')

    def __str__(self):
        return self.user.username

class Friend(models.Model):
    friend = models.OneToOneField(User, related_name='friend')

    def __str__(self):
        return self.friend.username

class Friendships(models.Model):
    friend1 = models.ForeignKey(User)
    friend2 = models.ForeignKey(Friend)
