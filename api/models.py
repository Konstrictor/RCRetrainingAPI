from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone

class Personnel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telephone = models.IntegerField()
	whatsapp_number = models.IntegerField()
	facebook_account = models.CharField(blank=True, max_length=60)
	tweeter_account = models.CharField(max_length=60, blank=True)
	instagram_account = models.CharField(max_length=60, blank=True)
	profile = models.CharField(max_length=60)
	detail = models.TextField()
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
	is_environmentalist = models.BooleanField(default=False)


class Depot(models.Model):
	quarter = models.CharField(max_length=60)
	longitude = models.FloatField()
	latitude = models.FloatField()

	def __str__(self):
		return self.quarter

class Source(models.Model):
	commune = models.CharField(max_length=60)
	quarter = models.CharField(max_length=60)
	description = models.CharField(max_length=60)
	longitude = models.FloatField()
	latitude = models.FloatField()
	is_valid = models.BooleanField(default=False)
	
	def __str__(self):
		return self.quarter


class Trajet(models.Model):
	"""docstring for Trajet"""
	source = models.ForeignKey(Source, null=False, on_delete=models.CASCADE)
	destination = models.ForeignKey(Depot, null=False, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.DateTimeField()

	def __str__(self):
		return f"{self.source} vers {self.destination}"

class Produit(models.Model):
	"""docstring for Produit"""
	product_tpye = models.CharField(max_length=60)
	quantity = models.FloatField()
	state = models.CharField(max_length=60)
	source = models.ForeignKey(Source, null=False, on_delete=models.CASCADE)

	def __str__(self):
		return self.product_tpye
		
		