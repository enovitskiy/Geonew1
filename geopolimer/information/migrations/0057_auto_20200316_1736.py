# Generated by Django 2.2.6 on 2020-03-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0056_auto_20200312_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='navconstruct',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='navconstruct',
            name='keywords',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='subnavigator',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='subnavigator',
            name='keywords',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='subsubnav',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='subsubnav',
            name='keywords',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]