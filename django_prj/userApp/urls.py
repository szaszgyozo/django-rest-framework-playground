from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from userApp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getuserprofilebyid/<id>/', get_user_profile_by_id),
    path('getuserprofiles/', get_user_profiles),
    path('getuserandprofilebyuser/', get_user_and_profile_by_user),
    path('getuserandprofiles/', get_user_and_profiles),
    path('saveuserprofile/', save_user_profile),
    path('deleteuserprofile/', delete_user_profile),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]