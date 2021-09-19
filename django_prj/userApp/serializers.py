from userApp.models import UserProfile
from rest_framework import serializers

class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'first_name', 'last_name', 'user_name']

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'phone_nr', 'age', 'status']