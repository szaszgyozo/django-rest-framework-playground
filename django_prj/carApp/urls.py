from django.urls import path
from carApp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
   path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('getcarbyid/<id>/', views.get_car_by_id), 
   path('getcarsbyowner/<owner_id>/', views.get_cars_by_owner), 
   path('getcarsandowners/', views.get_cars_and_owners), 
   path('getownercars/<owner_id>/', views.get_owner_cars), 
   path('addnewcartoowner/', views.add_new_car_to_owner), 
   path('deletecarbyid/<id>/', views.delete_car_by_id), 
   path('changecarowner/<car_id>/', views.change_car_owner), 
]