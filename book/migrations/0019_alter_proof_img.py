# Generated by Django 5.2 on 2025-04-26 12:10

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_delete_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='img',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage, upload_to='proof/'),
        ),
    ]
