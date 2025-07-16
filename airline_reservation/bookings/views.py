from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Passenger
from flights.models import Flight
from .forms import PassengerForm, BookingForm
import uuid

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == 'POST':
        passenger_form = PassengerForm(request.POST)
        booking_form = BookingForm(request.POST)
        
        if passenger_form.is_valid() and booking_form.is_valid():
            passenger = passenger_form.save()
            
            # Generate a unique booking reference
            booking_reference = 'BK' + uuid.uuid4().hex[:6].upper()
            
            # Calculate price based on selected seat class
            seat_class = booking_form.cleaned_data['seat_class']
            if seat_class == 'E':
                amount = flight.economy_price
            elif seat_class == 'B':
                amount = flight.business_price
            else:
                amount = flight.first_class_price
            
            # Create booking
            booking = Booking(
                booking_reference=booking_reference,
                user=request.user,
                flight=flight,
                passenger=passenger,
                seat_class=seat_class,
                amount_paid=amount,
            )
            booking.save()
            
            messages.success(request, f'Flight booked successfully! Your booking reference is {booking_reference}.')
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        passenger_form = PassengerForm()
        booking_form = BookingForm()
    
    return render(request, 'bookings/book_flight.html', {
        'flight': flight,
        'passenger_form': passenger_form,
        'booking_form': booking_form,
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'bookings/confirmation.html', {'booking': booking})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

