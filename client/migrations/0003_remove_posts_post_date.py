# Generated by Django 3.0.7 on 2020-09-19 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_posts_post_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_date',
        ),
    ]
