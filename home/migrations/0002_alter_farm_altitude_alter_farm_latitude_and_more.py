# Generated by Django 5.0.6 on 2024-06-14 18:00

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='altitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='latitude',
            field=models.DecimalField(decimal_places=16, max_digits=20),
        ),
        migrations.AlterField(
            model_name='farm',
            name='longitude',
            field=models.DecimalField(decimal_places=16, max_digits=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.profile_picture_path),
        ),
    ]
