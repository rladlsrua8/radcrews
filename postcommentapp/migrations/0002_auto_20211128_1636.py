# Generated by Django 3.2.7 on 2021-11-28 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
        ('postcommentapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='storage',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postcomment', to='postapp.post'),
        ),
    ]