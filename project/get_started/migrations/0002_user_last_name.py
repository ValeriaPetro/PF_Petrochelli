# Generated by Django 4.2.7 on 2023-12-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_started', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
