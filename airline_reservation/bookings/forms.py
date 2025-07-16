from django import forms
from .models import Passenger, Booking

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'email', 'phone', 'passport_number', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seat_class']
        labels = {
            'seat_class': 'Select Seat Class',
        }
        widgets = {
            'seat_class': forms.RadioSelect(),
        }
