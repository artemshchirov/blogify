from django.db.models import Model, TextField, DateTimeField, ForeignKey, CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(Model):
    text = TextField()
    pub_date = DateTimeField(auto_now_add=True)
    author = ForeignKey(User, on_delete=CASCADE, related_name='posts')
