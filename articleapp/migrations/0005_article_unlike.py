# Generated by Django 3.2.7 on 2021-10-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='unlike',
            field=models.IntegerField(default=0),
        ),
    ]
