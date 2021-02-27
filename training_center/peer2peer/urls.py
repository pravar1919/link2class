from .views import (
    marketing,
    todays_events_view, 
    upcoming_events_view, 
    ondemand_events_view,
    like_unlike_post_peer2peer
)
from django.urls import path

app_name = 'marketing'

urlpatterns = [
    path('',marketing, name='marketing'),
    path('liked/', like_unlike_post_peer2peer, name='like-post-view'),
    # path('today/<pk>/',todays_events_view, name='todays_events'),
    # path('upcoming/<pk>/',upcoming_events_view, name='upcoming_events'),
    # path('ondemand/<pk>/',ondemand_events_view, name='ondemand_events'),
]