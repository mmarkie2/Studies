# Generated by Django 3.0.3 on 2020-02-06 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'cities'},
        ),
    ]
