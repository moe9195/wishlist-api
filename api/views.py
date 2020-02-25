from django.shortcuts import render
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import IsItemAdder
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import ListSerializer, DetailSerializer, RegisterSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["image", "name", "description"]
    # search_fields = '__all__'
    ordering_fields = ["image", "name", "description"]
    # ordering_fields = '__all__'
    permission_classes = [AllowAny]

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "item_id"
    permission_classes = [IsItemAdder]

class Register(CreateAPIView):
    serializer_class = RegisterSerializer
