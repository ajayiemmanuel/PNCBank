# Generated by Django 4.2.4 on 2023-09-04 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar', models.CharField(default='0', max_length=200, null=True)),
                ('euro', models.CharField(default='0', max_length=200)),
                ('inr', models.CharField(default='0', max_length=200)),
                ('notification_number', models.CharField(default='0', max_length=200)),
                ('notification_message', models.CharField(default='0', max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]