# Generated by Django 4.1.5 on 2023-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_video_file_product_video_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video_duration',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='en_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='ru_price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
