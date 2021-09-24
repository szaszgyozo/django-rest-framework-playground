
from carApp.models import CarOwner
from userApp.serializers import SimpleUserSerializer
from rest_framework import serializers
from carApp.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarOwnerSerializer(serializers.ModelSerializer):
    owner = SimpleUserSerializer() 
    cars = CarSerializer(many=True)
    class Meta:
        model = CarOwner
        fields = ['owner', 'cars']
