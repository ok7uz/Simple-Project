from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.event.models import Relative, Event
from apps.event.serializers import RelativeSerializer, EventSerializer, VoteSerializer


class RelativeListView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        tags=['Relative'],
        responses={200: RelativeSerializer(many=True)},
    )
    def get(self, request):
        relatives = request.user.relatives.all()
        serializer = RelativeSerializer(relatives, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Relative'],
        responses={200: RelativeSerializer},
        request=RelativeSerializer,
    )
    def post(self, request):
        serializer = RelativeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventListView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        tags=['Event'],
        responses={200: EventSerializer(many=True)},
    )
    def get(self, request):
        relatives = request.user.events.all()
        serializer = EventSerializer(relatives, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Event'],
        responses={200: EventSerializer},
        request=EventSerializer,
    )
    def post(self, request):
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteView(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        tags=['Vote'],
        responses={200: VoteSerializer(many=True)},
    )
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        votes = event.votes.all()
        serializer = VoteSerializer(votes, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        tags=['Vote'],
        responses={200: VoteSerializer},
        request=VoteSerializer,
    )
    def post(self, request, event_id):
        serializer = VoteSerializer(data=request.data, context={'request': request, 'event_id': event_id})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
