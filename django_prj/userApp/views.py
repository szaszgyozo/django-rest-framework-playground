from django.http import response
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from userApp.models import UserProfile
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from userApp.serializers import UserProfileSerializer, SimpleUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def get_save_delete_user_profile_by_id(request, pk):
    try:
        user = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)

    # get a userprofile
    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return response(serializer.data)
    # update a userprofile
    if request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a single userprofile
    if request.method == 'DELETE':
        user.delete()
        return response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_user_profiles(request):
    return
def get_user_and_profile_by_user(request):
    return
def get_user_and_profiles(request):
    return
def save_user_profile(request):
    return
def delete_user_profile(request):
    return
def create_user_profile (request):
    return
