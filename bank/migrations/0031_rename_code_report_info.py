# Generated by Django 4.2.4 on 2023-09-06 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0030_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='code',
            new_name='info',
        ),
    ]