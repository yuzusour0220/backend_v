# Generated by Django 5.0.6 on 2024-08-28 23:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0022_alter_members_photo_alter_shushoaisatsu_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
