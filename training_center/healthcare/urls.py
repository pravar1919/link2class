from .views import (
    health_and_medicine,
    todays_events_view, 
    upcoming_events_view, 
    ondemand_events_view,
    like_unlike_post_health
)
from django.urls import path

app_name = 'healthcare'

urlpatterns = [
    path('',health_and_medicine, name='health'),
    path('today/<pk>/',todays_events_view, name='todays_events'),
    path('upcoming/<pk>/',upcoming_events_view, name='upcoming_events'),
    path('ondemand/<pk>/',ondemand_events_view, name='ondemand_events'),
    path('liked/', like_unlike_post_health, name='like-post-view'),

]