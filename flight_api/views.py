from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Function Based Views Below

@api_view(['GET'])
def find_flight(request):
    bodyData = request.data
    req_flight = Flight.objects.filter(
        departureCity = bodyData['departureCity'],
        arrivalCity = bodyData['arrivalCity'],
        dateOfDeparture = bodyData['dateOfDeparture']
    )
    serialized_flight = FlightSerializer(req_flight, many=True)
    return Response(serialized_flight.data)


@api_view(['POST'])
def save_reservation(request):
    bodyData = request.data
    req_flight = Flight.objects.get(id= bodyData['flightID'])

    req_passenger = Passenger()
    req_passenger.firstName = bodyData['firstName']
    req_passenger.lastName = bodyData['lastName']
    req_passenger.middlename = bodyData['middleName']
    req_passenger.email = bodyData['email']
    req_passenger.phone = bodyData['phone']
    req_passenger.save()

    req_reservation = Reservation()
    req_reservation.flight = req_flight
    req_reservation.passenger = req_passenger
    req_reservation.save()

    return Response(status=status.HTTP_201_CREATED)


# Non Primary based Operations Below

class ListFlight(ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ListPassengers(ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ListReservation(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


# Primary Key based Operation Below 


class DetailedFlight(RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class DetailedPassenger(RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class Detailedreservation(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer