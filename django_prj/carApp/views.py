from django.contrib.auth.models import User
from carApp.serializers import CarOwnerSerializer
from carApp.models import CarOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from carApp.models import Car
from rest_framework.response import Response
from rest_framework import status
from carApp.serializers import CarSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_car_by_id(request, id):
    try:
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cars_by_owner(request, owner_id): 
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    cars = Car.objects.all().filter(owner=owner)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cars_and_owners(request):
    try:
        cars_and_owners = CarOwner.objects.all()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = CarOwnerSerializer(cars_and_owners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_owner_cars(request, owner_id):    
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    cars = Car.objects.all().filter(owner=owner)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_new_car_to_owner(request): 
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_car_by_id(request, id): 
    try: 
        car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_car_owner(request, car_id):
    try: 
        car = Car.objects.get(pk=car_id)
        owner = CarOwner.objects.get(owner=request.user)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except CarOwner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    car.owner_id = owner.id
    car.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
