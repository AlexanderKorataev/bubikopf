# Generated by Django 4.1.5 on 2023-01-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='video/'),
        ),
    ]
