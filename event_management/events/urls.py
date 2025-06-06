from django.urls import path
from .views import (
    CreateEvent,
    ListEvent,
    UserListEvent,
    ListUpcomingEvent,
    UpdateEvent,
    DeleteEvent,
    RegisterEvent,
    UnregisterEvent,
    ListRegisteredEvent,
)

urlpatterns = [
    path("createEvent/", CreateEvent.as_view(), name="create-event"),
    path("listEvent/", ListEvent.as_view(), name="list-event"),
    path("myEvent/", UserListEvent.as_view(), name="my-event"),
    path("upcoming/Event/", ListUpcomingEvent.as_view(), name="upcoming-event"),
    path("update/Event/<int:pk>/", UpdateEvent.as_view(), name="update-event"),
    path("delete/Event/<int:pk>/", DeleteEvent.as_view(), name="delete-event"),
    path("register/Event/", RegisterEvent.as_view(), name="register-event"),
    path(
        "unregister/Event/<int:pk>/", UnregisterEvent.as_view(), name="unregister-event"
    ),
    path("registeredEvent/", ListRegisteredEvent.as_view(), name="registered-event"),
]
