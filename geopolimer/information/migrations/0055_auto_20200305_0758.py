# Generated by Django 2.2.6 on 2020-03-05 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0054_auto_20200304_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnavigator',
            name='hreflogo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subsubnav',
            name='hreflogo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]