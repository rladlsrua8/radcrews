# Generated by Django 3.2.7 on 2022-04-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0006_alter_comment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
