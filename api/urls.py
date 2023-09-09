# Dans le fichier urls.py de votre application

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HotelViewSet, RoomViewSet, BookingViewSet, ReviewViewSet, FacilityViewSet, ResidenceTypeViewSet, ResidenceViewSet, ResidenceRoomViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'residence-types', ResidenceTypeViewSet)
router.register(r'residences', ResidenceViewSet)
router.register(r'residence-rooms', ResidenceRoomViewSet)


urlpatterns = [
    path('', include(router.urls)),
]   

# Créer un nouvel hôtel en effectuant une requête POST vers /api/hotels/.
# Lire la liste de tous les hôtels en effectuant une requête GET vers /api/hotels/.
# Lire les détails d'un hôtel spécifique en effectuant une requête GET vers /api/hotels/{hotel_id}/.
# Mettre à jour un hôtel en effectuant une requête PUT ou PATCH vers /api/hotels/{hotel_id}/.
# Supprimer un hôtel en effectuant une requête DELETE vers /api/hotels/{hotel_id}/.