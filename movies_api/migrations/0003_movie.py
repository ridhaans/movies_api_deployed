# Generated by Django 2.1.3 on 2018-11-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0002_moviemanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('duration', models.DurationField()),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
            ],
        ),
    ]