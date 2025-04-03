# Event Management API

This Django-based event management application enables users to create, update, delete, and view upcoming events. Users can also register and unregister for events, view their registered events, and manage event details.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bernadettechukwuedo/Event-Manager.git
   ```

2. Navigate to the project directory:

   ```bash
    cd event_management
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the server:

   ```bash
   python manage.py runserver

   ```

## Features

- **Apps**

  - accounts
  - events

- **Models**

  - Event model
  - User model

## URL Endpoints

| URL                             | View                    | Description                                   |
| ------------------------------- | ----------------------- | --------------------------------------------- |
| `api/register/`                 | `register()`            | Handles user registration.                    |
| `api/login/`                    | `login_user()`          | Handles user login.                           |
| `api/logout/`                   | `logout()`              | Logs out the user.                            |
| `events/createEvent/`           | `CreateEvent()`         | Allow users to create an event                |
| `events/listEvent/`             | `ListEvent()`           | Display all events                            |
| `events/myEvent/`               | `UserListEvent()`       | Allows users to see their events              |
| `events/upcoming/Event/`        | `ListUpcomingEvent()`   | Allows users to list upcoming events          |
| `events/update/Event/<int:pk>/` | `UpdateEvent()`         | Allows event creators to update their events. |
| `events/delete/Event/<int:pk>/` | `DeleteEvent()`         | Allows event creators to delete their events. |
| `register/Event/`               | `RegisterEvent()`       | Allows users to register for an event.        |
| `unregister/Event/<int:pk>/`    | `UnregisterEvent()`     | Allows users to unregister for an event.      |
| `registeredEvent/`              | `ListRegisteredEvent()` | Allows users to view their registered events. |

## Usage

To interact with the API, you can use [Postman](https://www.postman.com/).

### Register for an Event

**Endpoint:** `POST /api/register/`

**Headers:**

- `Authorization: Bearer <token>`

**Body:**

```json
{
  "fields": "field_detail"
}
```

## Check it out

[![Check out the app](https://img.shields.io/badge/Check%20it%20Out-Here-4CAF50?style=flat-square)](https://your-deployed-app-link.com)
