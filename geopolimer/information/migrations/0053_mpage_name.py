# Generated by Django 2.2.6 on 2020-03-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0052_mpage_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpage',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]