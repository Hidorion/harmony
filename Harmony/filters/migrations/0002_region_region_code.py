# Generated by Django 3.1.2 on 2020-12-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='region_code',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=False,
        ),
    ]
