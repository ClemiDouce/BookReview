from django.contrib import admin

# Register your models here.
from follows.models import UserFollows

admin.site.register(UserFollows)
