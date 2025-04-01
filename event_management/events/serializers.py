from .models import Event, Registration
from rest_framework import serializers
import datetime
from django.db.models import F


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "location",
            "capacity",
            "created_by",
            "organizer",
            "created_date",
            "updated_date",
            "date",
            "time",
        ]
        read_only_fields = ["id", "created_by", "created_date", "updated_date"]

    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError("Capacity must be greater than 0")
        return value

    def validate_date(self, value):
        if value <= datetime.date.today():
            raise serializers.ValidationError("The event date must be in the future.")
        return value


