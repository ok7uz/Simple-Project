from django.urls import path

from apps.event.views import RelativeListView, RelativeDetailView, EventListView, VoteView

urlpatterns = [
    path('relatives/', RelativeListView.as_view(), name='relatives'),
    path('relatives/<uuid:relative_id>/', RelativeDetailView.as_view(), name='relative-detail'),
    path('events/', EventListView.as_view(), name='events'),
    path('events/<uuid:event_id>/votes/', VoteView.as_view(), name='vote'),
]
