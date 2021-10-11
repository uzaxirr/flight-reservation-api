from django.urls import path
from .views import ListFlight, DetailedFlight, ListPassengers, DetailedPassenger, ListReservation, Detailedreservation, find_flight, save_reservation
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('flights', ListFlight.as_view()),
    path('flight/<int:pk>', DetailedFlight.as_view()),
    path('passengers', ListPassengers.as_view()),
    path('passenger/<int:pk>', DetailedPassenger.as_view()),
    path('reservations', ListReservation.as_view()),
    path('reservation/<int:pk>', Detailedreservation),
    path('find/', find_flight),
    path('save/', save_reservation),
    path('token/', obtain_auth_token)
]