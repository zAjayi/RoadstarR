from django.contrib import admin
from .models import CarStore
from .models import UserInfo
from .models import ContactInfo
from .models import FeaturedCars

# Register your models here.
admin.site.register(CarStore)
admin.site.register(UserInfo)
admin.site.register(ContactInfo)
admin.site.register(FeaturedCars)