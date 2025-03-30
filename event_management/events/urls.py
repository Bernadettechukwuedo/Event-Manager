from django.urls import path
from .views import CreateEvent, ListEvent

urlpatterns = [path("createEvent/", CreateEvent.as_view(), name="create-event"),
               path("listEvent/", ListEvent.as_view(), name="list-event")]
