from django.urls import path
from . import views

urlpatterns = [

    # Routes pour les biens (Properties)
    path('api/properties/', views.PropertyList.as_view(), name='property-list'),
    path('api/properties/<int:pk>/', views.PropertyDetail.as_view(), name='property-detail'),

    # Routes pour les réservations (Bookings)
    path('api/bookings/', views.BookingList.as_view(), name='booking-list'),
    path('api/bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),

    # Routes pour les commentaires (Reviews)
    path('api/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('api/reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),


    # Routes pour les équipements (Amenities)
    path('api/amenities/', views.AmenityList.as_view(), name='amenity-list'),
    path('api/amenities/<int:pk>/', views.AmenityDetail.as_view(), name='amenity-detail'),

    # Routes pour les règles de la maison (HouseRules)
    path('api/houserules/', views.HouseRulesList.as_view(), name='houserules-list'),
    path('api/houserules/<int:pk>/', views.HouseRulesDetail.as_view(), name='houserules-detail'),

    # Routes pour les images des biens (PropertyImages)
    path('api/propertyimages/', views.PropertyImageList.as_view(), name='propertyimage-list'),
    path('api/propertyimages/<int:pk>/', views.PropertyImageDetail.as_view(), name='propertyimage-detail'),

    # Routes pour les notifications (Notifications)
    path('api/notifications/', views.NotificationList.as_view(), name='notification-list'),
    path('api/notifications/<int:pk>/', views.NotificationDetail.as_view(), name='notification-detail'),

    # Routes pour les signalements (Reports)
    path('api/reports/', views.ReportList.as_view(), name='report-list'),
    path('api/reports/<int:pk>/', views.ReportDetail.as_view(), name='report-detail'),

    # Routes pour les transactions (Transactions)
    path('api/transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]
