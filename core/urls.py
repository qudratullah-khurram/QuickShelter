from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),

    # Landlords
    path("landlords/", views.LandlordListView.as_view(), name="landlord-list"),
    path("landlords/add/", views.LandlordCreateView.as_view(), name="landlord-add"),
    path("landlords/<int:pk>/", views.LandlordDetailView.as_view(), name="landlord-detail"),
    path("landlords/<int:pk>/edit/", views.LandlordUpdateView.as_view(), name="landlord-edit"),
    path("landlords/<int:pk>/delete/", views.LandlordDeleteView.as_view(), name="landlord-delete"),

    # Properties
    path("properties/", views.PropertyListView.as_view(), name="property-list"),
    path("properties/add/", views.PropertyCreateView.as_view(), name="property-add"),
    path("properties/<int:pk>/", views.PropertyDetailView.as_view(), name="property-detail"),
    path("properties/<int:pk>/edit/", views.PropertyUpdateView.as_view(), name="property-edit"),
    path("properties/<int:pk>/delete/", views.PropertyDeleteView.as_view(), name="property-delete"),

    # Tenants
    path("tenants/", views.TenantListView.as_view(), name="tenant-list"),
    path("tenants/add/", views.TenantCreateView.as_view(), name="tenant-add"),
    path("tenants/<int:pk>/", views.TenantDetailView.as_view(), name="tenant-detail"),
    path("tenants/<int:pk>/edit/", views.TenantUpdateView.as_view(), name="tenant-edit"),
    path("tenants/<int:pk>/delete/", views.TenantDeleteView.as_view(), name="tenant-delete"),
    path('accounts/signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]