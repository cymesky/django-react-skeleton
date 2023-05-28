from django.db import models


# Create your models here.
class Tile(models.Model):
    terrain = models.CharField(max_length=50)
    has_ruins = models.BooleanField()


class Enemy(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    speed = models.IntegerField()
    tile = models.ForeignKey(Tile, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Player(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    speed = models.IntegerField()
    tile = models.ForeignKey(Tile, on_delete=models.SET_NULL, null=True, blank=True, default=None)
