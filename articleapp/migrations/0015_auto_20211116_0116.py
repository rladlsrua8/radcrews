# Generated by Django 3.2.7 on 2021-11-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0014_auto_20211116_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='article/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='article/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='article/'),
        ),
    ]
