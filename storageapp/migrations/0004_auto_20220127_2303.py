# Generated by Django 3.2.7 on 2022-01-27 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storageapp', '0003_alter_storage_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='upload',
        ),
        migrations.AddField(
            model_name='storage',
            name='attached',
            field=models.FileField(default=django.utils.timezone.now, upload_to='storage/'),
            preserve_default=False,
        ),
    ]