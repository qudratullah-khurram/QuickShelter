# core/forms.py
from django import forms
from .models import Landlord, Property, Tenant

class LandlordForm(forms.ModelForm):
    class Meta:
        model = Landlord
        fields = ["name", "address", "phone_number", "email"]

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ["title", "address", "property_type", "rent_amount", "rent_frequency", "landlord"]

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ["name", "passport_number", "email", "phone", "tenancy_start", "tenancy_end", "property"]
        widgets = {
            "tenancy_start": forms.DateInput(attrs={"type":"date"}),
            "tenancy_end": forms.DateInput(attrs={"type":"date"}),
        }