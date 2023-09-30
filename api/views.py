from rest_framework import generics, status
from .models import*
from .serializers import*

from rest_framework.response import Response
# List des chambres 
class ChambreList(generics.ListCreateAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):

        # Votre logique de filtrage basée sur l'utilisateur connecté
        # Par exemple, si vous souhaitez filtrer les propriétés de l'utilisateur connecté :
        queryset = Property.objects.all()

        return queryset
    
# List des images des chambres
class ImagehotelList(generics.ListCreateAPIView):
    serializer_class = ImagehotelSerializer

    def get_queryset(self):
        # Obtenez l'utilisateur connecté
        user = self.request.user    

        # Votre logique de filtrage basée sur l'utilisateur connecté
        # Par exemple, si vous souhaitez filtrer les propriétés de l'utilisateur connecté :
        queryset = Imagehotel.objects.filter(owner=user)

        return queryset

    def perform_create(self, serializer):
        # Appel à la méthode perform_create de la classe parente pour effectuer la création de l'objet
        user = self.request.user
        instance = serializer.save(owner=user)

        # Vous pouvez personnaliser le message de création ici
        message = f'La propriété avec l\'ID {instance.id} a été créée avec succès.'

        # Vous pouvez également personnaliser le statut de réponse HTTP ici (par exemple, 201 Created personnalisé)
        response_data = {
            'message': message,
            'data': serializer.data  # Inclure les données sérialisées dans la réponse si nécessaire
        }
        print(response_data)
        # Utilisez le statut HTTP personnalisé que vous souhaitez (par exemple, 201 Created personnalisé)
        return Response(response_data, status=status.HTTP_201_CREATED)
    

class PropertyList(generics.ListCreateAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        # Obtenez l'utilisateur connecté
        user = self.request.user    

        # Votre logique de filtrage basée sur l'utilisateur connecté
        # Par exemple, si vous souhaitez filtrer les propriétés de l'utilisateur connecté :
        queryset = Property.objects.filter(owner=user)

        return queryset

    def perform_create(self, serializer):
        # Appel à la méthode perform_create de la classe parente pour effectuer la création de l'objet
        user = self.request.user
        instance = serializer.save(owner=user)

        # Vous pouvez personnaliser le message de création ici
        message = f'La propriété avec l\'ID {instance.id} a été créée avec succès.'

        # Vous pouvez également personnaliser le statut de réponse HTTP ici (par exemple, 201 Created personnalisé)
        response_data = {
            'message': message,
            'data': serializer.data  # Inclure les données sérialisées dans la réponse si nécessaire
        }
        print(response_data)
        # Utilisez le statut HTTP personnalisé que vous souhaitez (par exemple, 201 Created personnalisé)
        return Response(response_data, status=status.HTTP_201_CREATED)
    

class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_update(self, serializer):
        # Appel à la méthode perform_update de la classe parente pour effectuer la mise à jour de l'objet
        instance = serializer.save()

        # Vous pouvez personnaliser le message de mise à jour ici
        message = f'La propriété avec l\'ID {instance.id} a été mise à jour avec succès.'

        # Vous pouvez également personnaliser le statut de réponse HTTP ici (par exemple, 200 OK personnalisé)
        response_data = {
            'message': message,
            'data': serializer.data  # Inclure les données sérialisées dans la réponse si nécessaire
        }

        # Utilisez le statut HTTP personnalisé que vous souhaitez (par exemple, 200 OK personnalisé)
        return Response(response_data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        # Appel à la méthode perform_destroy de la classe parente pour effectuer la suppression de l'objet
        instance.delete()

        # Vous pouvez personnaliser le message de suppression ici
        message = f'La propriété avec l\'ID {instance.id} a été supprimée avec succès.'

        # Vous pouvez également personnaliser le statut de réponse HTTP ici (par exemple, 204 No Content personnalisé)
        response_data = {'message': message}

        # Utilisez le statut HTTP personnalisé que vous souhaitez (par exemple, 204 No Content personnalisé)
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)   

class PropertyTypeList(generics.ListCreateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'Le type de propriété avec l\'ID {instance.id} a été créé avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class PropertyTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'Le type de propriété avec l\'ID {instance.id} a été mis à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'Le type de propriété avec l\'ID {instance.id} a été supprimé avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Obtenez l'utilisateur connecté
        user = self.request.user

        # Assignez l'utilisateur à la réservation lors de la création
        serializer.save(client=user)

        # Message personnalisé de création
        message = f'La réservation a été créée avec succès pour l\'utilisateur {user}.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'La réservation avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'La réservation avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Message personnalisé de création
        message = f'L\'avis avec l\'ID {instance.id} a été créé avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_update(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de mise à jour
        message = f'L\'avis avec l\'ID {instance.id} a été mis à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'L\'avis avec l\'ID {instance.id} a été supprimé avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


class PropertyImageList(generics.ListCreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'L\'image de propriété avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class PropertyImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'L\'image de propriété avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'L\'image de propriété avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


class AmenityList(generics.ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Message personnalisé de création
        message = f'L\'équipement avec l\'ID {instance.id} a été créé avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class AmenityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'L\'équipement avec l\'ID {instance.id} a été mis à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'L\'équipement avec l\'ID {instance.id} a été supprimé avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


class HouseRulesList(generics.ListCreateAPIView):
    queryset = HouseRules.objects.all()
    serializer_class = HouseRulesSerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'Les règles de la maison avec l\'ID {instance.id} ont été créées avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class HouseRulesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseRules.objects.all()
    serializer_class = HouseRulesSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'Les règles de la maison avec l\'ID {instance.id} ont été mises à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'Les règles de la maison avec l\'ID {instance.id} ont été supprimées avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)

class PropertyAvailabilityList(generics.ListCreateAPIView):
    queryset = PropertyAvailability.objects.all()
    serializer_class = PropertyAvailabilitySerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'La disponibilité de la propriété avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class PropertyAvailabilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PropertyAvailability.objects.all()
    serializer_class = PropertyAvailabilitySerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'La disponibilité de la propriété avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'La disponibilité de la propriété avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Message personnalisé de création
        message = f'La transaction avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'La transaction avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'La transaction avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)

class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        user=self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'Le rapport avec l\'ID {instance.id} a été créé avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'Le rapport avec l\'ID {instance.id} a été mis à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'Le rapport avec l\'ID {instance.id} a été supprimé avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        user=self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'La notification avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Message personnalisé de mise à jour
        message = f'La notification avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'La notification avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        user = self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de création
        message = f'La Room avec l\'ID {instance.id} a été créée avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_201_CREATED)

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_update(self, serializer):
        user=self.request.user
        instance = serializer.save(owner=user)

        # Message personnalisé de mise à jour
        message = f'La Room avec l\'ID {instance.id} a été mise à jour avec succès.'

        return Response({'message': message, 'data': serializer.data}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

        # Message personnalisé de suppression
        message = f'La Room avec l\'ID {instance.id} a été supprimée avec succès.'

        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)






