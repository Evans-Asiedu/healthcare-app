# Generated by Django 4.1.2 on 2023-08-25 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcare', '0009_customuser_image_alter_appointment_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 20, 35, 44, 137982, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 20, 35, 44, 136982, tzinfo=datetime.timezone.utc)),
        ),
    ]
