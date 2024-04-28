from django.contrib import admin

from apps.event.models import Event, Relative, Vote


admin.site.register(Relative)
admin.site.register(Event)
admin.site.register(Vote)
