# Generated by Django 3.2.3 on 2021-05-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_polulando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
