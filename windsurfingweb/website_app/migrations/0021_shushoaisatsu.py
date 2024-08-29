# Generated by Django 5.0.6 on 2024-08-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0020_alter_schedule_mitei'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shushoaisatsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名前')),
                ('message', models.TextField(verbose_name='メッセージ')),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
                ('status', models.CharField(choices=[('主将', '主将'), ('元主将', '元主将')], max_length=10, verbose_name='種類')),
            ],
        ),
    ]
