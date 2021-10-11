from django.urls import path
from .views import ListFlight, DetailedFlight, ListPassengers, DetailedPassenger, ListReservation, Detailedreservation, find_flight, save_reservation

urlpatterns = [
    path('flights', ListFlight.as_view()),
    path('flight/<int:pk>', DetailedFlight.as_view()),
    path('passengers', ListPassengers.as_view()),
    path('passenger/<int:pk>', DetailedPassenger.as_view()),
    path('reservations', ListReservation.as_view()),
    path('reservation/<int:pk>', Detailedreservation),
    path('find/', find_flight),
    path('save/', save_reservation),
]