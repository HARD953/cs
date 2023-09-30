from django.db import models
from custumer.models import NewUser


# Modèle pour les types de biens
class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle pour les biens
class Property(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)  # L'utilisateur est le propriétaire du bien
    title = models.CharField(max_length=200)
    etoile=models.DecimalField(max_digits=10, decimal_places=2)
    nombre_chambre = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    description = models.TextField()
    # Autres champs comme les règles de la maison, les images, etc.

    def __str__(self):
        return self.title
            
class Imagehotel(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    bien = models.ForeignKey(Property, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='property_images/')
    image2 = models.ImageField(upload_to='property_images/')
    image3 = models.ImageField(upload_to='property_images/')
    image4 = models.ImageField(upload_to='property_images/')

# Modèle pour les biens
class Room(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)  # L'utilisateur est le propriétaire du bien
    hotel = models.ForeignKey(Property, on_delete=models.CASCADE)  # L'utilisateur est le propriétaire du bien
    description = models.TextField()
    capacite = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='property_images/')
    image2 = models.ImageField(upload_to='property_images/')
    equipement = models.ManyToManyField('Amenity', blank=True)
    disponibilite=models.BooleanField(default=True)
    # Autres champs comme les règles de la maison, les images, etc.

    def __str__(self):
        return self.capacite
    
# Modèle pour les types d'utilisateurs (clients et gestionnaires)
class UserType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Modèle pour les réservations
class Booking(models.Model):
    client = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    bien = models.ForeignKey(Property, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_arrive = models.DateField()
    date_depart = models.DateField()
    adulte = models.DecimalField(max_digits=10, decimal_places=2)
    enfant = models.DecimalField(max_digits=10, decimal_places=2)    
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs liés à la réservation

# Modèle pour les commentaires
class Review(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()  # Peut être un champ à choix pour les étoiles, par exemple

# Modèle pour les équipements
class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle pour les règles de la maison
class HouseRules(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    bien = models.ForeignKey(Property, on_delete=models.CASCADE)
    regles = models.TextField()

# Modèle pour les images des biens
class PropertyImage(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    bien = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

# Modèle pour les notifications
class Notification(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Modèle pour les signalements
class Report(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(NewUser, related_name='reported_user', on_delete=models.CASCADE)
    reason = models.TextField()

# Modèle pour la disponibilité des biens
class PropertyAvailability(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)           
    bien = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)


# Modèle pour les transactions financières
class Transaction(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs relatifs à la transaction si nécessaire
