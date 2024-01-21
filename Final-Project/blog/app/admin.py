from django.contrib import admin

from .models import Post, Subscriber

# Register your models here.
admin.site.register(Post)
admin.site.register(Subscriber)