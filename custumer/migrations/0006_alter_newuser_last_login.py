# Generated by Django 4.1.4 on 2023-09-30 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0005_alter_newuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 9, 14, 54, 250773, tzinfo=datetime.timezone.utc), verbose_name='last_login'),
        ),
    ]