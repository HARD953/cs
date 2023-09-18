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
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    amenities = models.ManyToManyField('Amenity', blank=True)
    # Autres champs comme les règles de la maison, les images, etc.

    def __str__(self):
        return self.title

# Modèle pour les types d'utilisateurs (clients et gestionnaires)
class UserType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Modèle pour les réservations
class Booking(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs liés à la réservation

# Modèle pour les commentaires
class Review(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()  # Peut être un champ à choix pour les étoiles, par exemple

# Modèle pour les équipements
class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle pour les règles de la maison
class HouseRules(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rules = models.TextField()

# Modèle pour les images des biens
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

# Modèle pour les notifications
class Notification(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Modèle pour les signalements
class Report(models.Model):
    reporter = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    reported_user = models.ForeignKey(NewUser, related_name='reported_user', on_delete=models.CASCADE)
    reason = models.TextField()

# Modèle pour la disponibilité des biens
class PropertyAvailability(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)


# Modèle pour les transactions financières
class Transaction(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Ajoutez d'autres champs relatifs à la transaction si nécessaire
