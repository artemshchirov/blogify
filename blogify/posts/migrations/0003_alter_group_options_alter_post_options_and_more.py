# Generated by Django 4.2.1 on 2023-05-12 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_group_post_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Public date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Post content'),
        ),
    ]
