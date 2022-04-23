from rest_framework.response import Response
from userApp.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from userApp.serializers import ExtendedUserProfileSerializer, UserProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_by_id(request, id):
    try:
        user = UserProfile.objects.get(pk=id)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profiles(request):
    try:
        profiles = UserProfile.objects.all()
    except: 
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = UserProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_and_profile_by_user(request):
    try:
        profile = UserProfile.objects.get(user_id=request.user)   
    except: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ExtendedUserProfileSerializer(profile)
    return Response(serializer.data)     



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_and_profiles(request):
    try:
        profiles = UserProfile.objects.all()
    except: 
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = ExtendedUserProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def save_user_profile(request):
    try:
        user = UserProfile.objects.get(user_id=request.user)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = UserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def delete_user_profile(request):
    try:
        userProfile = UserProfile.objects.get(user_id=request.user)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    userProfile.status = 0
    userProfile.save()

    return Response(status=status.HTTP_204_NO_CONTENT)







