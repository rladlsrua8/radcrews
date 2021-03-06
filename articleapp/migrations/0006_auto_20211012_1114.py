# Generated by Django 3.2.7 on 2021-10-12 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0005_article_unlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='article/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleapp.article')),
            ],
        ),
    ]
