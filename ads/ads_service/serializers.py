from rest_framework import serializers
from .models import User, Advertisement, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'email', 'user_password', 'location']

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'ad_text', 'location', 'author', 'is_public']

    def to_representation(self, instance):
        representation = super(AdSerializer, self).to_representation(instance)
        representation['location'] = instance.location.location_name
        representation['author'] = instance.author.login
        return representation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'