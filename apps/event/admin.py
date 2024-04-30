from django.contrib import admin

from apps.event.models import Event, Relative, Vote


@admin.register(Relative)
class RelativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'id', 'phone_number')
    list_filter = ('user',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'id')
    list_filter = ('user',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('event', 'relative', 'id', 'type')
    list_filter = ('event',)
