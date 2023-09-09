from django.contrib import admin
from .models import*
# Register your models here.


admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Facility)
admin.site.register(ResidenceType)
admin.site.register(Residence)
admin.site.register(ResidenceRoom)
