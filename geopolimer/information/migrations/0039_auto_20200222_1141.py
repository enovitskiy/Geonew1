# Generated by Django 2.2.6 on 2020-02-22 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0038_auto_20200222_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageproject',
            old_name='blockquote',
            new_name='blockquote1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='paragraph',
            new_name='paragraph1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='textnext',
            new_name='textnext1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='titlecoloumn',
            new_name='titlecoloumn1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='titlenext',
            new_name='titlenext1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='titleparagraph',
            new_name='titleparagraph1',
        ),
        migrations.RenameField(
            model_name='pageproject',
            old_name='urlvideo',
            new_name='urlvideo1',
        ),
    ]
