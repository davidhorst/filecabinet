from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^properties$', views.properties, name="properties"),
    url(r'^add_property$', views.add_property, name="add_property"),

    url(r'^property/(?P<prop_id>\d+)/events$', views.events, name="events"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)$', views.event, name="event_by_id"),
    url(r'^property/(?P<prop_id>\d+)/add_event$', views.add_event, name="add_events"),

    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/alert/(?P<alert_id>\d+)$', views.alert, name="alert"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/add_alert$', views.add_alert, name="add_alert"),

    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/note/(?P<note_id>\d+)$', views.note, name="note"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/notes$', views.notes, name="notes"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/add_note$', views.add_note, name="add_note"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/note/(?P<note_id>\d+)/update_note$', views.update_note, name="update_note"),
    url(r'^property/(?P<prop_id>\d+)/event/(?P<event_id>\d+)/note/(?P<note_id>\d+)/add_file$', views.add_file, name="add_file"),

    url(r'^sidebar$', views.sidebar, name="sidebar"),
    url(r'^attachment/(?P<file_id>\d+)$', views.get_file, name="attachment"),
]
