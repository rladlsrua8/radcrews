# Generated by Django 3.2.7 on 2021-12-03 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0015_auto_20211116_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='project',
            new_name='specialty',
        ),
    ]
