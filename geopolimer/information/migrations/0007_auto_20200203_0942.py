# Generated by Django 2.2.6 on 2020-02-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_auto_20200203_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigator',
            name='subname',
        ),
        migrations.AddField(
            model_name='navigator',
            name='subname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='information.Subnavigator'),
        ),
    ]