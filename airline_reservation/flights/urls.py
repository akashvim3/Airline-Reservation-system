from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.FlightSearchView.as_view(), name='search'),
    path('flight/<int:pk>/', views.FlightDetailView.as_view(), name='flight_detail'),
]
