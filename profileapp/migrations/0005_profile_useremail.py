# Generated by Django 3.2.7 on 2021-12-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_remove_profile_radiologist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='useremail',
            field=models.EmailField(max_length=128, null=True),
        ),
    ]