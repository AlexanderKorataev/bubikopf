# Generated by Django 4.1.5 on 2023-01-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_name', models.CharField(max_length=255)),
                ('en_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='lesson_')),
                ('ru_description', models.TextField(blank=True, null=True)),
                ('en_description', models.TextField(blank=True, null=True)),
                ('ru_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('en_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]