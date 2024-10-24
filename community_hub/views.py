from django.shortcuts import render, get_object_or_404
from .models import Event
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .forms import EventForm

# Create your views here.
class EventListView(ListView):
    model = Event
    template_name = 'community_hub/events_list.html'
    context_object_name = 'events'
    
class CreateEventView(FormView):
    template_name = "community_hub/events_form.html"
    form_class = EventForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EventDetailView(DetailView):
    model = Event
    template_name = "community_hub/event_detail.html"
    