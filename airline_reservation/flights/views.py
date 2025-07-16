from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils import timezone  # Add this import
from .models import Flight, Airport

def home(request):
    airports = Airport.objects.all()
    featured_flights = Flight.objects.filter(departure_time__gte=timezone.now())[:6]
    return render(request, 'flights/home.html', {
        'airports': airports,
        'featured_flights': featured_flights
    })

class FlightSearchView(ListView):
    model = Flight
    template_name = 'flights/search_results.html'
    context_object_name = 'flights'
    
    def get_queryset(self):
        queryset = Flight.objects.filter(departure_time__gte=timezone.now())
        
        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        departure_date = self.request.GET.get('departure_date')
        
        if origin:
            queryset = queryset.filter(origin__code=origin)
        if destination:
            queryset = queryset.filter(destination__code=destination)
        if departure_date:
            queryset = queryset.filter(departure_time__date=departure_date)
            
        return queryset

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flights/flight_detail.html'