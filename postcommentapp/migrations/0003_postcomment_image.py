# Generated by Django 3.2.7 on 2021-12-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postcommentapp', '0002_auto_20211128_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='postcomment/'),
        ),
    ]