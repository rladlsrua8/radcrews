# Generated by Django 3.2.7 on 2021-12-05 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0016_rename_project_article_specialty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='specialty',
            new_name='project',
        ),
    ]
