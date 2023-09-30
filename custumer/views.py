from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

class NewUserList(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Message personnalisé de création
        message = f'La NewUser avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class NewUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'L\'utilisateur avec l\'ID {instance.id} a été mis à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'L\'utilisateur avec l\'ID {instance.id} a été supprimé avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)


# from social_django.utils import psa

# @psa()
# def google_login(request, backend):
#     """
#     Redirects the user to Google for authentication.
#     """
#     return request.backend.redirect()

# @psa()
# def google_callback(request, backend):
#     """
#     Handles the callback from Google after authentication.
#     """
#     user = request.backend.do_auth(request.GET.get('access_token'))
#     # Handle user authentication as needed
#     # ...
