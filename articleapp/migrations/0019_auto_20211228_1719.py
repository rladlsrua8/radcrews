# Generated by Django 3.2.7 on 2021-12-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0018_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='article/%Y/%m/%d'),
        ),
    ]
