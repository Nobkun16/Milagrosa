# Generated by Django 5.2 on 2025-04-26 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_alter_proof_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proof',
            name='hash',
        ),
    ]
