# Event Management System

A RESTful backend for browsing and booking events, built with Django and Django REST Framework. Users register and log in with JWT authentication, admins manage events, and attendees book them with built-in checks for balance, capacity, and duplicate bookings.

## Tech Stack

- Python, Django, Django REST Framework
- SimpleJWT (JWT authentication with token blacklisting)
- django-filter (filtering, search, and ordering)
- SQLite

## Features

- **Authentication:** registration, login, and logout with JWT access/refresh tokens. Logout blacklists the refresh token so it can no longer be used. Tokens can be refreshed at `/event_management/token/refresh/`.
- **Password reset:** request a reset token by email, then set a new password using the token (Django's token generator).
- **Role-based permissions:** any authenticated user can view events, but only admins (staff) can create, edit, or delete them (custom `IsAdminOrReadOnly` permission).
- **Event management:** CRUD for events, with validation that capacity and price are greater than zero.
- **Booking rules:** a booking is rejected if the attendee's balance is lower than the event price, the event is at capacity, or the attendee has already booked it. A database unique constraint also blocks duplicate bookings.
- **Search, filter, and order:** filter events by location, capacity, and price; search by name, description, and location; order by name, date, price, and capacity.
- **Pagination:** list endpoints are paginated (5 items per page).

## Data Model

| Model | Key fields |
|---|---|
| `Event` | name, description, date, location, capacity, price |
| `Attendee` | user (one-to-one with Django `User`), name, email, phone, birthday, balance |
| `Booking` | attendee (FK), event (FK), booked_at, payment_method (Visa / InstaPay / Apple Pay) |

`Booking` has a unique constraint on (`attendee`, `event`).

## API Endpoints

All endpoints below return JSON. Resource endpoints support the standard REST actions (list, create, retrieve, update, delete).

### Authentication (`/authentication/`)

| Method | Endpoint | Description |
|---|---|---|
| POST | `/authentication/register/` | Create an account (username, email, password) |
| POST | `/authentication/login/` | Get access and refresh tokens |
| POST | `/authentication/logout/` | Blacklist a refresh token (requires login) |
| POST | `/authentication/forgetPassword/` | Email a password reset token |
| PATCH | `/authentication/updatePassword/<user_id>/` | Set a new password using the reset token |
| POST | `/event_management/token/refresh/` | Get a new access token |

### Resources (`/event_management/`, login required)

| Endpoint | Notes |
|---|---|
| `/event_management/events/` | Read: any logged-in user. Write: admin only. Supports `?location=`, `?price=`, `?capacity=`, `?search=`, `?ordering=` |
| `/event_management/attendees/` | Manage attendee profiles |
| `/event_management/bookings/` | Create and manage bookings (validated against balance, capacity, and duplicates) |

Send the access token with each request:

```
Authorization: Bearer <access_token>
```

## Getting Started

1. Clone the repository and create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install django djangorestframework djangorestframework-simplejwt django-filter
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. (Optional) Create an admin user, needed to create events:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

The API is then available at `http://127.0.0.1:8000/`.

### Password reset emails

The password reset flow sends email through Django's `send_mail`, so configure the `EMAIL_*` settings in `config/settings.py`. For local testing, you can print emails to the console instead by adding:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

## Project Structure

```text
Event_Management_System/
├── authentication/        # Register, login, logout, password reset, custom permissions
├── event_management/      # Event, Attendee, Booking models, serializers, views
├── config/                # Project settings and root URLs
└── manage.py
```