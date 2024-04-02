from rest_framework import serializers
from api.models import Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
