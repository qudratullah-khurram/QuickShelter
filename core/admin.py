
from django.contrib import admin
from .models import Landlord, Property, Tenant

# admin.site.register(Landlord)
# admin.site.register(Property)
# admin.site.register(Tenant)


@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "created_by", "created_at")
    search_fields = ("name", "email", "phone_number")

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "property_type", "rent_amount", "rent_frequency", "landlord", "created_by")
    list_filter = ("property_type", "rent_frequency")

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "passport_number", "property", "tenancy_start", "tenancy_end", "created_by")
    search_fields = ("name", "passport_number")
