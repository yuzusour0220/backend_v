# Generated by Django 5.0.6 on 2024-08-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0011_rename_schedulefile_resultpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultpdf',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
