# Generated by Django 4.0.1 on 2022-01-31 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_post_banco'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='banco2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='banco', to='blog.banco'),
        ),
    ]
