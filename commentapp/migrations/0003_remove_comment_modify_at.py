# Generated by Django 3.2.7 on 2021-11-28 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0002_auto_20211126_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modify_at',
        ),
    ]