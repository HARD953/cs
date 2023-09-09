# Dans le fichier views.py de votre application

from rest_framework import viewsets
from .models import User, Hotel, Room, Booking, Review, Facility, ResidenceType, Residence, ResidenceRoom
from .serializers import UserSerializer, HotelSerializer, RoomSerializer, BookingSerializer, ReviewSerializer, FacilitySerializer, ResidenceTypeSerializer, ResidenceSerializer, ResidenceRoomSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class ResidenceTypeViewSet(viewsets.ModelViewSet):
    queryset = ResidenceType.objects.all()
    serializer_class = ResidenceTypeSerializer

class ResidenceViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer

class ResidenceRoomViewSet(viewsets.ModelViewSet):
    queryset = ResidenceRoom.objects.all()
    serializer_class = ResidenceRoomSerializer
