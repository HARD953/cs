from rest_framework import generics
from .models import*
from .serializers import*

class PropertyList(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PropertyImageList(generics.ListCreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

class PropertyImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

class AmenityList(generics.ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class AmenityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

class HouseRulesList(generics.ListCreateAPIView):
    queryset = HouseRules.objects.all()
    serializer_class = HouseRulesSerializer

class HouseRulesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseRules.objects.all()
    serializer_class = HouseRulesSerializer

class PropertyAvailabilityList(generics.ListCreateAPIView):
    queryset = PropertyAvailability.objects.all()
    serializer_class = PropertyAvailabilitySerializer

class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer






