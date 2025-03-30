from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.timezone import now


# Create your views here.
class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ListEvent(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


class UserListEvent(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(created_by=user)


class ListUpcomingEvent(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        today = now().date()
        return Event.objects.filter(date__gt=today)
