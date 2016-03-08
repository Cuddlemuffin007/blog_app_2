"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from blog_app.views import Home, PostCreateView, SignUpView, AuthorPostView, TagCreateView, like_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home_view'),
    url(r'^author/(?P<pk>\d+)/posts$', AuthorPostView.as_view(), name='author_post_view'),
    url(r'^login/$', auth_views.login, name='login_view'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout_view'),
    url(r'^sign_up/$', SignUpView.as_view(), name='signup_view'),
    url(r'^create_post/$', login_required(PostCreateView.as_view()), name='post_create_view'),
    url(r'^post/(?P<pk>\d+)/create_tag/$', TagCreateView.as_view(), name='tag_create_view'),
    url(r'^post/(?P<pk>\d+)/like/$', like_view, name='like_view')
]
