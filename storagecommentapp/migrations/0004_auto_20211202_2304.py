# Generated by Django 3.2.7 on 2021-12-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagecommentapp', '0003_auto_20211202_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storagecomment',
            name='upload',
        ),
        migrations.AddField(
            model_name='storagecomment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='storagecomment/'),
        ),
    ]