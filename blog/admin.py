from django.contrib import admin
from .models import Post, Comment    # . means it is in this app

# Register your models here.
admin.site.register(Post);
admin.site.register(Comment);
