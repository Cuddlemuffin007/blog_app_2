from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from blog_app.models import Post, Author


class Home(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body')

    def form_valid(self, form):
        post_object = form.save(commit=False)
        post_object.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home_view')

