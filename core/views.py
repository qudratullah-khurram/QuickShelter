# core/views.py
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Landlord, Property, Tenant
from .forms import LandlordForm, PropertyForm, TenantForm
from django.db.models import Prefetch
from django.shortcuts import render, redirect

class Home(LoginView):
    template_name = 'home.html'

class OwnedObjectMixin(UserPassesTestMixin):
    """Mixin to ensure object belongs to current user (created_by) or is related."""
    def test_func(self):
        obj = self.get_object()
        # Accept operations if the user created the object
        try:
            return obj.created_by == self.request.user
        except AttributeError:
            return False

# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # show landlords, properties, tenants created by user
        user = self.request.user
        ctx["landlords"] = Landlord.objects.filter(created_by=user)
        ctx["properties"] = Property.objects.filter(created_by=user).select_related("landlord")
        ctx["tenants"] = Tenant.objects.filter(created_by=user).select_related("property")
        return ctx

# Landlord Views
class LandlordListView(LoginRequiredMixin, ListView):
    model = Landlord
    template_name = "landlords/landlord_list.html"
    context_object_name = "landlords"

    def get_queryset(self):
        return Landlord.objects.filter(created_by=self.request.user)

class LandlordDetailView(LoginRequiredMixin, DetailView):
    model = Landlord
    template_name = "landlords/landlord_detail.html"

    def get_queryset(self):
        return Landlord.objects.filter(created_by=self.request.user).prefetch_related("properties")

class LandlordCreateView(LoginRequiredMixin, CreateView):
    model = Landlord
    form_class = LandlordForm
    template_name = "landlords/landlord_form.html"
    success_url = reverse_lazy("landlord-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LandlordUpdateView(LoginRequiredMixin, OwnedObjectMixin, UpdateView):
    model = Landlord
    form_class = LandlordForm
    template_name = "landlords/landlord_form.html"
    success_url = reverse_lazy("landlord-list")

class LandlordDeleteView(LoginRequiredMixin, OwnedObjectMixin, DeleteView):
    model = Landlord
    template_name = "landlords/landlord_confirm_delete.html"
    success_url = reverse_lazy("landlord-list")

# Property Views
class PropertyListView(LoginRequiredMixin, ListView):
    model = Property
    template_name = "properties/property_list.html"
    context_object_name = "properties"

    def get_queryset(self):
        return Property.objects.filter(created_by=self.request.user).select_related("landlord")

class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property
    template_name = "properties/property_detail.html"

    def get_queryset(self):
        return Property.objects.filter(created_by=self.request.user).select_related("landlord").prefetch_related("tenants")

class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "properties/property_form.html"
    success_url = reverse_lazy("property-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, OwnedObjectMixin, UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "properties/property_form.html"
    success_url = reverse_lazy("property-list")

class PropertyDeleteView(LoginRequiredMixin, OwnedObjectMixin, DeleteView):
    model = Property
    template_name = "properties/property_confirm_delete.html"
    success_url = reverse_lazy("property-list")

# Tenant Views
class TenantListView(LoginRequiredMixin, ListView):
    model = Tenant
    template_name = "tenants/tenant_list.html"
    context_object_name = "tenants"

    def get_queryset(self):
        return Tenant.objects.filter(created_by=self.request.user).select_related("property")

class TenantDetailView(LoginRequiredMixin, DetailView):
    model = Tenant
    template_name = "tenants/tenant_detail.html"

    def get_queryset(self):
        return Tenant.objects.filter(created_by=self.request.user).select_related("property")

class TenantCreateView(LoginRequiredMixin, CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = "tenants/tenant_form.html"
    success_url = reverse_lazy("tenant-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TenantUpdateView(LoginRequiredMixin, OwnedObjectMixin, UpdateView):
    model = Tenant
    form_class = TenantForm
    template_name = "tenants/tenant_form.html"
    success_url = reverse_lazy("tenant-list")

class TenantDeleteView(LoginRequiredMixin, OwnedObjectMixin, DeleteView):
    model = Tenant
    template_name = "tenants/tenant_confirm_delete.html"
    success_url = reverse_lazy("tenant-list")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

