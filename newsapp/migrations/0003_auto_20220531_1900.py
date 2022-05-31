# Generated by Django 3.2.13 on 2022-05-31 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
