# Generated by Django 4.1.2 on 2023-08-17 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcare', '0003_alter_post_publication_date_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 12, 17, 2, 513366, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 17, 12, 17, 2, 513366, tzinfo=datetime.timezone.utc)),
        ),
    ]
