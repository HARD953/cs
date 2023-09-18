from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import generics

# Create your views here.
class NewUserList(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

class NewUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer