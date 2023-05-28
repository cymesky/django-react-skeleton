from django.shortcuts import render
from rest_framework import generics
from .models import Tile
from .serializers import TileSerializer

# Create your views here.
class TileView(generics.ListAPIView):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
