from django.urls import path
from .views import CreateEvent, ListEvent, UserListEvent, ListUpcomingEvent

urlpatterns = [
    path("createEvent/", CreateEvent.as_view(), name="create-event"),
    path("listEvent/", ListEvent.as_view(), name="list-event"),
    path("myEvent/", UserListEvent.as_view(), name="my-event"),
    path("upcoming/Event/", ListUpcomingEvent.as_view(), name="upcoming-event"),
]
