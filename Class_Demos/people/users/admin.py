# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

from .models import UserProfile, Friend, Friendships

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (u'id', u'user')
    list_filter = ('user',)
    raw_id_fields = ('friends',)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = (u'id', u'friend')
    list_filter = ('friend',)


@admin.register(Friendships)
class FriendshipsAdmin(admin.ModelAdmin):
    list_display = (u'id', u'friend1', u'friend2')
    list_filter = ('friend1', 'friend2')
