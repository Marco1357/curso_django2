# Generated by Django 3.2.2 on 2021-05-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('youtube_id', models.CharField(max_length=32)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
