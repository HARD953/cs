# Dans le fichier serializers.py de votre application

from rest_framework import serializers
from .models import User, Hotel, Room, Booking, Review, Facility, ResidenceType, Residence, ResidenceRoom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)  # Champ pour les chambres associées à l'hôtel
    class Meta:
        model = Hotel
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class ResidenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceType
        fields = '__all__'

class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields = '__all__'

class ResidenceRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceRoom
        fields = '__all__'
