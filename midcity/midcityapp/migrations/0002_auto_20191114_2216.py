# Generated by Django 2.2.6 on 2019-11-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midcityapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteership',
            name='hours',
            field=models.IntegerField(default=1),
        ),
    ]
