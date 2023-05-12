from django.db.models import (
    Model,
    TextField,
    DateTimeField,
    ForeignKey,
    CharField,
    SlugField,
    CASCADE,
    SET_NULL,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(Model):
    title = CharField(max_length=200, verbose_name="Title")
    slug = SlugField(unique=True)
    description = TextField(verbose_name="Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Post(Model):
    text = TextField(verbose_name="Post content")
    pub_date = DateTimeField(auto_now_add=True, verbose_name="Public date")
    author = ForeignKey(
        User, on_delete=CASCADE, related_name="posts", verbose_name="Author"
    )
    group = ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name="posts",
        verbose_name="Group",
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
