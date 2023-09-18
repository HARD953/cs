from django.urls import path
from . import views

urlpatterns = [

    # Routes pour les biens (Properties)
    path('api/custumer/', views.NewUserList.as_view(), name='custumer-list'),
    path('api/custumer/<int:pk>/', views.NewUserDetail.as_view(), name='custumer-detail'),
]