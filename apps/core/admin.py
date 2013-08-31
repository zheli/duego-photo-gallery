from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.core.models import Photo, Like

admin.site.register(Photo)
admin.site.register(Like)
