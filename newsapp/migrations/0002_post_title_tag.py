# Generated by Django 3.2.13 on 2022-05-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='newsblog', max_length=255),
        ),
    ]
