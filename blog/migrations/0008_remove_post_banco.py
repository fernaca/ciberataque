# Generated by Django 4.0.1 on 2022-01-31 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_banco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='banco',
        ),
    ]
