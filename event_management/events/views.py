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
