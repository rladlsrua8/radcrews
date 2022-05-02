# Generated by Django 3.2.7 on 2022-02-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storageapp', '0005_auto_20220206_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='upload',
        ),
        migrations.AddField(
            model_name='storage',
            name='attached',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name='첨부 파일'),
        ),
    ]
