# Generated by Django 3.1.3 on 2021-01-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20201228_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
