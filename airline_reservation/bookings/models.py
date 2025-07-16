from django.db import models
from django.contrib.auth.models import User
from flights.models import Flight

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    SEAT_CLASS_CHOICES = [
        ('E', 'Economy'),
        ('B', 'Business'),
        ('F', 'First Class'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
        ('R', 'Refunded'),
    ]
    
    booking_reference = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_class = models.CharField(max_length=1, choices=SEAT_CLASS_CHOICES)
    seat_number = models.CharField(max_length=5, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default='P')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.booking_reference} - {self.passenger}"

