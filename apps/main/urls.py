from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^properties$', views.properties, name="properties"),
    url(r'^properties/events$', views.events, name="events"),
    url(r'^properties/event/(?P<id>\d+)$', views.event, name="event_id"),
    url(r'^properties/events/add_event$', views.add_event, name="add_events"),
    url(r'^properties/note$', views.events, name="events"),
    url(r'^properties/events/note/add_note$', views.add_note, name="add_note"),
]
