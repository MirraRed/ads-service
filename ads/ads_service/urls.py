from django.urls import path
from .views import *

urlpatterns = [
    path('user/register/', register_user, name='register_user'), #
    path('user/<int:userId>/', get_user_by_id, name='get_user_by_id'),
    path('user/update/<int:userId>/', update_user_by_id, name='update_user_by_id'),
    path('user/delete/<int:userId>/', delete_user_by_id, name='delete_user_by_id'),
    path('ad/', get_all_ads, name='get_all_ads'),
    path('ad/create/', create_ad, name='create_ad'), #
    path('ad/<int:adId>/', get_ad_by_id, name='get_ad_by_id'),
    path('ad/update/<int:adId>/', edit_advertisement, name='edit_advertisement'),
    path('ad/delete/<int:adId>/', delete_advertisement, name='delete_advertisement'),
    path('location/create/', create_location, name='create_location'), #
    path('location/', get_all_locations, name='get_all_locations'),
    path('location/<int:locationId>/', get_location_by_id, name='get_location_by_id'),
    path('location/update/<int:locationId>/', update_location_by_id, name='update_location_by_id'),
    path('location/delete/<int:locationId>/', delete_location_by_id, name='delete_location_by_id'),

]
