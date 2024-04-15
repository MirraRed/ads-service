from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Advertisement, Location
from .serializers import UserSerializer, AdSerializer, LocationSerializer

@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
    else:
        # GET request, display registration form
        return render(request, 'register_user.html', {'form': UserSerializer()})

@api_view(['GET'])
def get_user_by_id(request, userId):
    try:
        user = User.objects.get(id=userId)
    except User.DoesNotExist:
        return Response({"error": "Користувача не знайдено за вказаним id"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return render(request, 'user_detail.html', {'user': serializer.data}, content_type='text/html')

@api_view(['PUT'])
def update_user_by_id(request, userId):
    try:
        user = User.objects.get(id=userId)
    except User.DoesNotExist:
        return Response({"error": "Користувача не знайдено за вказаним id"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

    serializer = UserSerializer(user)
    return render(request, 'user/user_update.html', {'user': user, 'serializer': serializer})


@api_view(['GET', 'DELETE'])
def delete_user_by_id(request, userId):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=userId)
        except User.DoesNotExist:
            return Response({"error": "Користувача не знайдено за вказаним id"}, status=status.HTTP_404_NOT_FOUND)

        return render(request, 'delete_user.html', {'user': user})

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=userId)
        except User.DoesNotExist:
            return Response({"error": "Користувача не знайдено за вказаним id"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": f"Користувач із заданою id ({userId}) успішно видалений"},
                        status=status.HTTP_200_OK, content_type='application/json')

@api_view(['GET'])
def get_all_ads(request):
    page = request.query_params.get('page', 1)
    limit = request.query_params.get('limit', 10)
    visibility = request.query_params.get('visibility', 'public')

    ads = Advertisement.objects.filter(is_public=(visibility == 'public'))
    serializer = AdSerializer(ads, many=True)

    context = {
        'ads': serializer.data,
        'page': page,
        'limit': limit,
        'visibility': visibility,
    }

    return render(request, 'get_all_ads.html', context)

@api_view(['GET', 'POST'])
def create_ad(request):
    if request.method == 'POST':
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        locations = Location.objects.all()
        users = User.objects.all()
        return render(request, 'create_ad.html', {'locations': locations, 'users': users})

@api_view(['GET'])
def get_ad_by_id(request, adId):
    try:
        ad = Advertisement.objects.get(id=adId)
    except Advertisement.DoesNotExist:
        return Response({"error": "Оголошення не знайдено"}, status=status.HTTP_404_NOT_FOUND)

    return render(request, 'get_ad_by_id.html', {'ad': ad})


@api_view(['GET', 'PUT'])
def edit_advertisement(request, adId):
    try:
        ad = Advertisement.objects.get(id=adId)
    except Advertisement.DoesNotExist:
        return Response({"error": "Оголошення не знайдено"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'edit_advertisement.html', {'ad': ad})

@api_view(['GET', 'DELETE'])
def delete_advertisement(request, adId):
    try:
        ad = Advertisement.objects.get(id=adId)
    except Advertisement.DoesNotExist:
        return Response({"error": "Оголошення не знайдено"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        ad.delete()
        return Response({"message": "Оголошення успішно видалено"}, status=status.HTTP_200_OK)
    else:
        return render(request, 'delete_advertisement.html', {'ad': ad})

@api_view(['GET', 'POST'])
def create_location(request):
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request, 'create_location.html')

@api_view(['GET'])
def get_all_locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return render(request, 'get_all_locations.html', {'locations': serializer.data})

@api_view(['GET'])
def get_location_by_id(request, locationId):
    try:
        location = Location.objects.get(id=locationId)
    except Location.DoesNotExist:
        return Response({"error": "Локація не знайдена за данною id адресою"}, status=status.HTTP_404_NOT_FOUND)

    return render(request, 'get_location_by_id.html', {'location': location})

@api_view(['GET', 'PUT'])
def update_location_by_id(request, locationId):
    try:
        location = Location.objects.get(id=locationId)
    except Location.DoesNotExist:
        return Response({"error": "Локація не знайдена за данною id адресою"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return render(request, 'edit_location.html', {'location': location})

@api_view(['GET', 'DELETE'])
def delete_location_by_id(request, locationId):
    try:
        location = Location.objects.get(id=locationId)
    except Location.DoesNotExist:
        return Response({"error": "Локація не знайдена за данною id адресою"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        location.delete()
        return Response({"message": "Локація успішно видалена"}, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        return render(request, 'delete_location.html', {'location': location})