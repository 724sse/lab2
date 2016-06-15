from django.db import models
from datetime import datetime

class Ware(models.Model):
    name = models.TextField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Receiver(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Supply(models.Model):
    ware_id = models.ForeignKey(Ware)
    supplier_id = models.ForeignKey(Supplier)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

class Shipment(models.Model):
    ware_id = models.ForeignKey(Ware)
    receiver_id = models.ForeignKey(Receiver)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)
