from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from blog_app.models import Post, Author


class Home(ListView):
    model = Post


class AuthorPostView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(author__user_id=self.kwargs['pk'])


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body')

    def form_valid(self, form):
        post_object = form.save(commit=False)
        post_object.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home_view')


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login_view')

