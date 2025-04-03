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


class RegisterEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["user", "event"]
        read_only_fields = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = instance.user.username
        data["event"] = instance.event.title

        return data

    def validate(self, data):
        get_event = data["event"]
        get_user = self.context["request"].user

        if get_event.created_by == get_user:
            raise serializers.ValidationError(
                "You cannot register for an event you created."
            )
        if Registration.objects.filter(event=get_event, user=get_user).exists():
            raise serializers.ValidationError(
                {"error": "You have already registered for this event."}
            )

        if get_event.capacity <= 0:
            raise serializers.ValidationError("Event is full")

        return data

    def create(self, validated_data):
        event = validated_data["event"]
        user = self.context["request"].user
        # To update in the database and not only in the python's memory
        updated = Event.objects.filter(id=event.id, capacity__gt=0).update(
            capacity=F("capacity") - 1
        )
        if not updated:
            raise serializers.ValidationError("Event is full")

        return Registration.objects.create(event=event, user=user)


