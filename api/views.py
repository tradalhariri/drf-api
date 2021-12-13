from rest_framework import generics
from items.models import Item
from .serializers import ItemSerializer


class ItemAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class ItemDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


