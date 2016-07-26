from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^properties$', views.properties, name="properties"),
    url(r'^add_property$', views.add_property, name="add_property"),

    url(r'^property/(?P<prop_id>\d+)/events$', views.events, name="events"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)$', views.event, name="event_id"),
    url(r'^property/(?P<prop_id>\d+)/add_event$', views.add_event, name="add_events"),

    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/note/(?P<note_id>\d+)$', views.note, name="note"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/notes$', views.notes, name="notes"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/note/(?P<note_id>\d+)/add_note$', views.add_note, name="add_note"),
]
