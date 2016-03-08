from django.contrib import admin

from blog_app.models import Post, Author, Tag

admin.site.register([Author, Post, Tag])
