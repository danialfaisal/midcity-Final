# Generated by Django 2.2.6 on 2019-11-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midcityapp', '0002_auto_20191114_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
