from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return "{}'s Author instance".format(self.user.username)


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    author = models.ForeignKey(Author)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.author.user.username)


@receiver(post_save, sender='auth.User')
def create_author(sender, **kwargs):
    print(kwargs)
    user_instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        Author.objects.create(user=user_instance)
