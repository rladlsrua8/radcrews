# Generated by Django 3.2.7 on 2021-10-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0012_auto_20211029_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='article/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
