# Generated by Django 4.2.4 on 2023-09-05 16:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0019_rename_transaction1_transaction1s_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction2s',
            new_name='Transaction1',
        ),
        migrations.RenameModel(
            old_name='Transaction1s',
            new_name='Transaction2',
        ),
    ]