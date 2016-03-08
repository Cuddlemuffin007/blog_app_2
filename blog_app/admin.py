from django.contrib import admin

from blog_app.models import Post, Author

admin.site.register([Author, Post])
