from django.urls import path

from apps.event.views import RelativeListView, EventListView, VoteView

urlpatterns = [
    path('relatives/', RelativeListView.as_view(), name='relatives'),
    path('events/', EventListView.as_view(), name='events'),
    path('events/<uuid:event_id>/votes/', VoteView.as_view(), name='vote'),
]
