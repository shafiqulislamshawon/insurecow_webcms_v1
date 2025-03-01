import uuid
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    investment_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    investment_period = models.CharField(max_length=50, null=True, blank=True)
    expected_return_min = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    expected_return_max = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_return_min = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    total_return_max = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to=f'portfolio_images/{category.name}/')
    description = models.TextField(null=True, blank=True)
    extra_data = models.JSONField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
