# Generated by Django 4.2.7 on 2023-11-26 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_newpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='newPost',
        ),
    ]