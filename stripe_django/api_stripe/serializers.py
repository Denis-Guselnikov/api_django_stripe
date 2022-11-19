from rest_framework import serializers

from products.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Item
