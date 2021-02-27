from .views import (
    construction, 
    todays_events_view, 
    upcoming_events_view, 
    ondemand_events_view,
    like_unlike_post_transition
 )

from django.urls import path

app_name = 'const'

urlpatterns = [
    path('',construction, name='const'),
    path('liked/', like_unlike_post_transition, name='like-post-view'),
    # path('today/<pk>/',todays_events_view, name='todays_events'),
    # path('upcoming/<pk>/',upcoming_events_view, name='upcoming_events'),
    # path('ondemand/<pk>/',ondemand_events_view, name='ondemand_events'),
]