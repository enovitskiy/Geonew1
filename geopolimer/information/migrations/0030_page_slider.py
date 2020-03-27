# Generated by Django 2.2.6 on 2020-02-10 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0029_auto_20200207_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hreflogo', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('text', models.TextField(blank=True)),
                ('quote', models.TextField(blank=True)),
                ('projname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtext', to='information.Subnavigator')),
                ('subname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text', to='information.Navconstruct')),
            ],
        ),
    ]