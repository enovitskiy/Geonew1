# Generated by Django 2.2.6 on 2020-03-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0049_pictslider_textslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='textslider',
            name='textbldown',
            field=models.TextField(blank=True),
        ),
    ]
