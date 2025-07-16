from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]
