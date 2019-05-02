# Generated by Django 2.1.4 on 2019-04-30 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190430_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 16, 26, 22, 454324, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 16, 26, 22, 453747, tzinfo=utc)),
        ),
    ]