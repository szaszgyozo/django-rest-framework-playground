from userApp.models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'phone_nr', 'age', 'status']

class ExtendedUserProfileSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()
    class Meta:
        model = UserProfile
        fields = [ 'phone_nr', 'age', 'status', 'user']

class AbcSerialzerr(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_nr', 'age', 'status', 'user_id']
        