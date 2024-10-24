from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('add_event', views.CreateEventView.as_view(), name="event_form"),
    path("<int:pk>", views.EventDetailView.as_view(), name="event_detail"),
]