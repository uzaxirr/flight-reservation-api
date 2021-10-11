from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.IntegerField()
    operatingAirline = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimitedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return self.departureCity

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.firstName

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.passenger