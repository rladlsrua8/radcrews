# Generated by Django 3.2.7 on 2022-04-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcommentapp', '0004_alter_postcomment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]