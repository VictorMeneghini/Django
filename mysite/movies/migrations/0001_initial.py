# Generated by Django 2.0 on 2019-01-16 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=0)),
                ('genre', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('poster', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ManyToManyField(to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
