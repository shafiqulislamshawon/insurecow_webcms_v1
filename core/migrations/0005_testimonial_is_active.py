# Generated by Django 5.1.6 on 2025-03-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
