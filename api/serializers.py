from rest_framework import serializers
from .models import Tile, Enemy, Player


class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ('terrain', 'has_ruins')


class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        fields = ('name', 'strength', 'speed', 'tile')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'strength', 'speed', 'tile')

