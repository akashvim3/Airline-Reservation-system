from django.db import models
from django.utils import timezone

class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Aircraft(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    registration = models.CharField(max_length=10, unique=True)
    economy_seats = models.PositiveIntegerField(default=0)
    business_seats = models.PositiveIntegerField(default=0)
    first_class_seats = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.airline.code} - {self.model} ({self.registration})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    economy_price = models.DecimalField(max_digits=10, decimal_places=2)
    business_price = models.DecimalField(max_digits=10, decimal_places=2)
    first_class_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='On Time', 
                             choices=[('On Time', 'On Time'), 
                                      ('Delayed', 'Delayed'),
                                      ('Cancelled', 'Cancelled'),
                                      ('Departed', 'Departed'),
                                      ('Arrived', 'Arrived')])
    
    def __str__(self):
        return f"{self.flight_number}: {self.origin.code} to {self.destination.code}"
    
    def duration(self):
        duration = self.arrival_time - self.departure_time
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m"

