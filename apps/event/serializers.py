from django.shortcuts import get_object_or_404
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
        fields = ['id', 'title', 'description',]

    def create(self, validated_data):
        user = self.context['request'].user
        return Event.objects.create(user=user, **validated_data)



class VoteSerializer(serializers.ModelSerializer):
    relative_id = serializers.UUIDField(source='relative.id', write_only=True)
    relative = RelativeSerializer(read_only=True)

    class Meta:
        model = Vote
        fields = ['relative_id', 'relative', 'type']

    def create(self, validated_data):
        event_id = self.context['event_id']
        relative_id = validated_data.pop('relative')['id']
        event = get_object_or_404(Event, id=event_id)
        relative = get_object_or_404(Relative, id=relative_id)
        validated_data['event'] = event
        validated_data['relative'] = relative
        return super().create(validated_data)
