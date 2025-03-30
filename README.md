# Event Management API

This Django-powered event application allows users to manage events by creating, updating, deleting, and viewing upcoming events.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bernadettechukwuedo/Event-Manager.git
   cd event_management
   pip install -r requirements.txt
   python manage.py runserver

   ```

## Features
-**Apps**
   - accounts
   - events

- **Models**

  - Event model
  - User model

## URL Endpoints

| URL                             | View                  | Description                                  |
| ------------------------------- | --------------------- | -------------------------------------------- |
| `api/register/`                 | `register()`          | Handles user registration.                   |
| `api/login/`                    | `login_user()`        | Handles user login.                          |
| `api/logout/`                   | `logout()`            | Logs out the user.                           |
| `events/createEvent/`           | `CreateEvent()`       | Allow users to create an event               |
| `events/listEvent/`             | `ListEvent()`         | Display all events                           |
| `events/myEvent/`               | `UserListEvent()`     | Allows users to see their events             |
| `events/upcoming/Event/`        | `ListUpcomingEvent()` | Allows users to list upcoming events         |
| `events/update/Event/<int:pk>/` | `UpdateEvent()`       | Allows event authors to update their events. |
| `events/delete/Event/<int:pk>/` | `DeleteEvent()`       | Allows event authors to delete their events. |
