# Generated by Django 3.2.7 on 2021-10-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_article_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]