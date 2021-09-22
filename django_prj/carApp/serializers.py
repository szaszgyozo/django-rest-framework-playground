
from carApp.models import CarOwner
from django_prj.userApp.serializers import SimpleUserSerializer
from rest_framework import serializers
from carApp.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarOwnerSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer() 
    car = CarSerializer()
    class Meta:
        model = CarOwner
        fields = ['user', 'car']