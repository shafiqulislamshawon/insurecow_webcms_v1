from django.db import models

class InsuranceType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserSubmission(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE, related_name="submissions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.insurance_type.name}"


class DynamicFormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('email', 'Email'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
        ('choice', 'Choice'),
        ('textarea', 'Text Area'),
        ('file', 'File Upload')
    ]

    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE, related_name="form_fields")
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    required = models.BooleanField(default=True)
    choices = models.TextField(blank=True, null=True, help_text="Comma-separated values for choice fields")
    default_value = models.TextField(blank=True, null=True)
    help_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.label} ({self.field_type}) - {self.insurance_type.name}"


class DynamicFormResponse(models.Model):
    submission = models.ForeignKey(UserSubmission, on_delete=models.CASCADE, related_name="responses")
    field = models.ForeignKey(DynamicFormField, on_delete=models.CASCADE, related_name="responses")
    value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submission.name} - {self.field.label}: {self.value}"
