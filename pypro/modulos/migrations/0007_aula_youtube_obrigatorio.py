# Generated by Django 3.2.3 on 2021-05-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_youtube_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(max_length=32),
        ),
    ]
