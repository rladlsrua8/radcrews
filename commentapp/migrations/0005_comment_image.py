# Generated by Django 3.2.7 on 2021-11-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0004_remove_comment_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comment/'),
        ),
    ]