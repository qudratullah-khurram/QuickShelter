
# core/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

class Landlord(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="landlords")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    HOUSE = "House"
    FLAT = "Flat"
    BUNGALOW = "Bungalow"
    STUDIO = "Studio"
    VILLA = "Villa"
    PROPERTY_TYPE_CHOICES = [
        (HOUSE, HOUSE),
        (FLAT, FLAT),
        (BUNGALOW, BUNGALOW),
        (STUDIO, STUDIO),
        (VILLA, VILLA),
    ]

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    RENT_FREQUENCY_CHOICES = [(DAILY, DAILY), (WEEKLY, WEEKLY), (MONTHLY, MONTHLY)]

    title = models.CharField(max_length=200)
    address = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    rent_frequency = models.CharField(max_length=10, choices=RENT_FREQUENCY_CHOICES, default=MONTHLY)
    landlord = models.ForeignKey(Landlord, on_delete=models.SET_NULL, null=True, related_name="properties")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.address}"

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    passport_number = models.CharField(max_length=80, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    tenancy_start = models.DateField()
    tenancy_end = models.DateField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="tenants")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tenants")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.passport_number})"
