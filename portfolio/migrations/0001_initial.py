# Generated by Django 5.1.6 on 2025-02-22 07:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('investment_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=10)),
                ('investment_period', models.CharField(max_length=50)),
                ('expected_return_min', models.DecimalField(decimal_places=2, max_digits=5)),
                ('expected_return_max', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_return_min', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_return_max', models.DecimalField(decimal_places=2, max_digits=15)),
                ('image', models.ImageField(upload_to='portfolio_images/None/')),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='portfolio.category')),
            ],
        ),
    ]
