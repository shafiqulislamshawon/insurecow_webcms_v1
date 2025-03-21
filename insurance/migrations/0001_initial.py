# Generated by Django 5.1.6 on 2025-02-24 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('field_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('email', 'Email'), ('date', 'Date'), ('boolean', 'Boolean'), ('choice', 'Choice'), ('textarea', 'Text Area'), ('file', 'File Upload')], max_length=20)),
                ('required', models.BooleanField(default=True)),
                ('choices', models.TextField(blank=True, help_text='Comma-separated values for choice fields', null=True)),
                ('default_value', models.TextField(blank=True, null=True)),
                ('help_text', models.CharField(blank=True, max_length=255, null=True)),
                ('insurance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='insurance.insurancetype')),
            ],
        ),
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('insurance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='insurance.insurancetype')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicFormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='insurance.dynamicformfield')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='insurance.usersubmission')),
            ],
        ),
    ]
