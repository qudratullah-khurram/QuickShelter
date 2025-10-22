# 🏡 QuickShelter

**QuickShelter** is a Django-based property management system designed for landlords, real estate agents, and short-term rental operators (like Airbnb hosts) to manage properties, tenants, and tenancy periods efficiently — all from a secure, multi-user web platform.

---

## ✅ Project Summary

QuickShelter simplifies the daily operations of rental businesses by offering a centralized, user-friendly dashboard for managing:
- Landlords
- Property listings
- Tenants and tenancy periods

Each user sees only their own data, with authentication and permissions handled securely via Django’s session-based auth.

---

## 🧩 Key Features

- **🔐 User Registration & Authentication**
  - Only registered users (agents) can access the platform
  - User-specific data isolation (each agent sees only their records)

- **🏘 Landlord Management**
  - Add, edit, and delete landlord profiles with full contact details

- **🏠 Property Management**
  - CRUD operations for properties: title, address, type, rent, and frequency
  - Link each property to a landlord

- **👤 Tenant Assignment**
  - Assign tenants to properties
  - Store tenant details: name, passport, contact info
  - Track tenancy periods (start & end dates)

- **📊 Dashboard**
  - Overview of all landlords, properties, and tenants tied to the logged-in user

- **🛡 Authorization**
  - Users can only access and manage data they have created or been assigned

---

## 🔄 Data Models & Relationships

### 📘 Landlord
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `name` | CharField | Full name of landlord |
| `address` | TextField | Landlord’s address |
| `phone_number` | CharField | Contact number |
| `email` | EmailField | Email address |

**Relationships:**
- One Landlord can have multiple Properties

---

### 🏠 Property
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `title` | CharField | Property name/title |
| `address` | TextField | Full property address |
| `property_type` | CharField (Choices) | House, Flat, Bungalow, etc. |
| `rent_amount` | DecimalField | e.g. 150.00 |
| `rent_frequency` | CharField (Choices) | Daily, Weekly, Monthly |
| `created_by` | ForeignKey → User | User who created this property |

**Relationships:**
- One Property belongs to one Landlord  
- One Property can have multiple Tenants

---

### 👤 Tenant
| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key |
| `name` | CharField | Full name |
| `passport_number` | CharField | Unique passport number |
| `email` | EmailField | Contact email |
| `phone` | CharField | Phone number |
| `tenancy_start` | DateField | Start date |
| `tenancy_end` | DateField | End date |
| `property` | ForeignKey → Property | Assigned property |

---

## 📚 User Stories

### 👨‍💼 As a Landlord or Agent:
- I want to securely log in and access my dashboard
- I want to create, edit, and delete properties
- I want to assign tenants to specific properties
- I want to view my properties and their current tenants
- I want to track tenancy dates
- I want to ensure my data is private and secure

---

## 🛠 Technical Stack

| Layer | Technology |
|-------|------------|
| Backend | Django |
| Database | PostgreSQL |
| Frontend | Django Templates + Custom CSS |
| Auth | Django's built-in session-based authentication |

---

## 🔮 Future Enhancements

- ✅ Rent payment tracking (paid/unpaid logs)
- ✅ PDF contract uploads
- ✅ Email reminders for tenancy expirations
- ✅ Tenant self-registration and limited access
- ✅ Calendar view for tenancy timelines
- ✅ Full mobile responsiveness

---

## ✅ Summary

QuickShelter delivers a practical, scalable solution for managing rental properties. It showcases:
- Secure multi-user access with Django Auth
- Clean, customizable UI for business use
- Clear model relationships and CRUD operations
- A real-world use case that demonstrates strong Django development skills

---

