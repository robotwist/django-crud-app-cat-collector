# Generated by Django 5.1.7 on 2025-04-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(),
        ),
    ]
