# Dans le fichier models.py de votre application

from django.db import models
from decimal import Decimal

class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse_email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    role = models.CharField(max_length=50)

class Hotel(models.Model):
    nom_etablissement = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    coordonnees_geographiques = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotel_images/')  # Ajout d'une image pour l'hôtel
    gerant = models.ForeignKey(User, on_delete=models.CASCADE)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    type_de_chambre = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    equipements = models.TextField()
    tarif_journalier = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)  # Indique si la chambre est disponible
    image1 = models.ImageField(upload_to='images_de_la_chambre/',default='jpg')
    image2 = models.ImageField(upload_to='images_de_la_chambre/',default='jpg')
    image3 = models.ImageField(upload_to='images_de_la_chambre/',default='jpg')
    image4 = models.ImageField(upload_to='images_de_la_chambre/',default='jpg')
    image5 = models.ImageField(upload_to='images_de_la_chambre/',default='jpg')

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_debut_sejour = models.DateField()
    date_fin_sejour = models.DateField()
    nombre_invite = models.PositiveIntegerField()
    statut_reservation = models.CharField(max_length=50, choices=[
        ('en_attente', 'En Attente'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
    ])
    montant_total = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Montant total de la réservation

    def calculate_total_amount(self):
        if self.date_debut_sejour and self.date_fin_sejour and self.room:
            duration = (self.date_fin_sejour - self.date_debut_sejour).days
            self.montant_total = Decimal(duration) * self.room.tarif_journalier * Decimal(self.nombre_invite)
        else:
            self.montant_total = None

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    note = models.PositiveIntegerField()
    commentaire = models.TextField()


class Facility(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    equipement = models.CharField(max_length=100)
    description = models.TextField()

class ResidenceType(models.Model):
    libelle_type = models.CharField(max_length=100)
    description = models.TextField()

class Residence(models.Model):
    type = models.ForeignKey(ResidenceType, on_delete=models.CASCADE)
    nom_etablissement = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    coordonnees_geographiques = models.CharField(max_length=100)
    image = models.ImageField(upload_to='residence_images/')  # Ajout d'une image pour la résidence
    gerant = models.ForeignKey(User, on_delete=models.CASCADE)

class ResidenceRoom(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    type_de_chambre = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField()
    equipements = models.TextField()
    tarif_journalier = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)  # Indique si la chambre est disponible
    image1 = models.ImageField(upload_to='images_de_la_residence/',default='jpg1')
    image2 = models.ImageField(upload_to='images_de_la_residence/',default='jpg1')
    image3 = models.ImageField(upload_to='images_de_la_residence/',default='jpg1')
    image4 = models.ImageField(upload_to='images_de_la_residence/',default='jpg1')
    image5 = models.ImageField(upload_to='images_de_la_residence/',default='jpg1')

    # models.py

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Booking)
def update_booking_total_amount(sender, instance, **kwargs):
    instance.calculate_total_amount()
    instance.save()
