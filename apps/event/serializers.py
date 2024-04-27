from rest_framework import serializers

from apps.event.models import Relative, Event, Vote


class RelativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relative
        fields = ['id', 'name', 'phone_number', 'relationship']

    def create(self, validated_data):
        user = self.context['request'].user
        return Relative.objects.create(user=user, **validated_data)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        return Event.objects.create(user=user, **validated_data)


class VoteSerializer(serializers.ModelSerializer):
    event_id = serializers.IntegerField(source='event.id')
    relative_id = serializers.IntegerField(source='relative.id')

    class Meta:
        model = Vote
        fields = ['id', 'event_id', 'relative_id', 'type']

