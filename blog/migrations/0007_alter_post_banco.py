# Generated by Django 4.0.1 on 2022-01-31 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_banco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banco',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.banco'),
        ),
    ]
