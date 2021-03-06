# Generated by Django 2.2.6 on 2020-02-03 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_navigator_template_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subnavigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('section', models.TextField(null=True)),
                ('template_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='navigator',
            name='subname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='information.Subnavigator'),
        ),
    ]
