from django.db import models

# Create your models here.
class CarStore(models.Model):
    name = models.CharField(max_length=400)
    price = models.CharField(max_length=400)
    imageUrl = models.CharField(max_length=1000)

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'carStore'

class UserInfo(models.Model):
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    epassword = models.CharField(max_length=20)

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'userinfo'

class ContactInfo(models.Model):
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    emessage = models.CharField(max_length=20)

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'contactinfo'

class FeaturedCars(models.Model):
    name = models.CharField(max_length=400)
    price = models.CharField(max_length=400)
    imageUrl = models.CharField(max_length=1000)

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'featuredcars'