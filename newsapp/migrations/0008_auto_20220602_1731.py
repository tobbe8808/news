# Generated by Django 3.2.13 on 2022-06-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
