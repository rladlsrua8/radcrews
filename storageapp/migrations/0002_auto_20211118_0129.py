# Generated by Django 3.2.7 on 2021-11-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storageapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='upload2',
        ),
        migrations.AlterField(
            model_name='storage',
            name='upload',
            field=models.FileField(blank=True, upload_to='storage/'),
        ),
    ]