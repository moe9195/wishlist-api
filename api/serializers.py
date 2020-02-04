from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User


class AddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    favourited = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    added_by = AddedBySerializer()
    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'detail', 'favourited']
    
    def get_favourited(self, obj):
        return obj.favoriteitem_set.count()

class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'favourited_by']

    def get_favourited_by(self, obj):
        return AddedBySerializer(obj.favoriteitem_set.all(), many=True).data





    