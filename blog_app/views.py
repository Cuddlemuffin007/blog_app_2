from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from blog_app.models import Post, Author, Tag


class Home(ListView):
    model = Post


class AuthorPostView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(author__user_id=self.kwargs['pk'])


class PostByTagView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs['name'])


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body')

    def form_valid(self, form):
        post_object = form.save(commit=False)
        post_object.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home_view')


class TagCreateView(CreateView):
    model = Tag
    fields = ('name',)

    def form_valid(self, form):
        tag_object = form.save(commit=False)
        post = Post.objects.get(pk=self.kwargs['pk'])
        for tag in Tag.objects.all():
            if tag.name == tag_object.name:
                post.tags.add(tag)
                return HttpResponseRedirect('/')

        tag_object.save()
        post.tags.add(tag_object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home_view')


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login_view')


def like_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect('/')