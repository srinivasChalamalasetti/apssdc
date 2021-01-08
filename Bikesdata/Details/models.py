from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	impf = models.ImageField(upload_to="Profile/",default="profile.jpeg")

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)
		
class YourOrder(models.Model):
	wks = [('yes','Book Now'),('No','Cancel')]
	date = models.DateField()
	feedback = models.TextField()
	orderstatus = models.CharField(max_length=10,choices=wks)
	m = models.ForeignKey(User,on_delete=models.CASCADE)

# class Addbikes(models.Model):
# 	brands = [(" Hero"  , " Hero" ),("Honda", " Honda")]
# 	bike = [("Hero Splendor Plus", "Hero Splendor Plus")]
# 	fuel =[("petrol","petrol"),("desiel","desiel")]
# 	brandname = models.CharField(max_length=20,choices=brands)
# 	brandlogo = models.ImageField(upload_to = "brands/")
# 	bikemodel = models.CharField(max_length = 100,choices=bike)
# 	bikefrontimage = models.ImageField(upload_to = "bikes/")
# 	bikebackimage = models.ImageField(upload_to = "bikes/")
# 	bikerightimage = models.ImageField(upload_to = "bikes/")
# 	bikeleftimage = models.ImageField(upload_to = "bikes/")
# 	bikecost = models.FloatField()
# 	fueltype = models.CharField(max_length=30,choices=fuel)
# 	no_of_gares = models.IntegerField()
# 	bikelocation = models.CharField(max_length=100)
