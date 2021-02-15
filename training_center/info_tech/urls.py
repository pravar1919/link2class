from .views import (
    information_tech,
    todays_events_view, 
    upcoming_events_view, 
    ondemand_events_view
)
from django.urls import path

app_name = 'info_tech'

urlpatterns = [
    path('',information_tech, name='it'),
    path('today/<pk>/',todays_events_view, name='todays_events'),
    path('upcoming/<pk>/',upcoming_events_view, name='upcoming_events'),
    path('ondemand/<pk>/',ondemand_events_view, name='ondemand_events'),
]