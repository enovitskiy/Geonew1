# Generated by Django 2.2.6 on 2020-03-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0047_contact_contdecr'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='icon',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
