# Generated by Django 4.2.13 on 2024-07-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
