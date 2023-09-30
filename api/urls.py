from django.urls import path
from . import views

urlpatterns = [

    # Routes pour les biens (Properties)
    path('api/biens/', views.PropertyList.as_view(), name='property-list'),
    path('api/biens/<int:pk>/', views.PropertyDetail.as_view(), name='property-detail'),
    path('api/image/', views.ImagehotelList.as_view(), name='image'),

    path('api/list/', views.ChambreList.as_view(), name='list'),

    path('api/chambre/', views.RoomList.as_view(), name='room-list'),
    path('api/chambre/<int:pk>/', views.RoomDetail.as_view(), name='room-detail'),


    path('api/typebien/', views.PropertyTypeList.as_view(), name='propertype-list'),
    path('api/typebien/<int:pk>/', views.PropertyTypeDetail.as_view(), name='propertype-detail'),

    # Routes pour les réservations (Bookings)
    path('api/reservation/', views.BookingList.as_view(), name='booking-list'),
    path('api/reservation/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),

    # Routes pour les commentaires (Reviews)
    path('api/commentaire/', views.ReviewList.as_view(), name='review-list'),
    path('api/commentaire/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),


    # Routes pour les équipements (Amenities)
    path('api/equipement/', views.AmenityList.as_view(), name='amenity-list'),
    path('api/equipement/<int:pk>/', views.AmenityDetail.as_view(), name='amenity-detail'),

    # Routes pour les règles de la maison (HouseRules)
    path('api/regles/', views.HouseRulesList.as_view(), name='houserules-list'),
    path('api/regles/<int:pk>/', views.HouseRulesDetail.as_view(), name='houserules-detail'),

    # Routes pour les images des biens (PropertyImages)
    path('api/imagebien/', views.PropertyImageList.as_view(), name='propertyimage-list'),
    path('api/imagebien/<int:pk>/', views.PropertyImageDetail.as_view(), name='propertyimage-detail'),

    # Routes pour les notifications (Notifications)
    path('api/notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('api/notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),

    # Routes pour les signalements (Reports)
    path('api/signalement/', views.ReportList.as_view(), name='report-list'),
    path('api/signalement/<int:pk>/', views.ReportDetail.as_view(), name='report-detail'),

    # Routes pour les transactions (Transactions)
    path('api/transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]
