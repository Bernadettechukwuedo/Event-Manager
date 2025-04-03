from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from .serializers import (
    EventSerializer,
    RegisterEventSerializer,

)
from .models import Event, Registration
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from django.utils.timezone import now
from .permissions import IsAuthororReadonly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import F


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


class UpdateEvent(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthororReadonly]


class DeleteEvent(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthororReadonly]


class RegisterEvent(CreateAPIView):
    serializer_class = RegisterEventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


