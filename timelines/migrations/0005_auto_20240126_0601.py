# Generated by Django 3.1 on 2024-01-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelines', '0004_auto_20240126_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]
