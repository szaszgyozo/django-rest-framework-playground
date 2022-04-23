from django.urls import path
from userApp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getuserprofilebyid/<id>/', views.get_user_profile_by_id),
    path('getuserprofiles/', views.get_user_profiles),
    path('getuserandprofilebyuser/', views.get_user_and_profile_by_user),
    path('getuserandprofiles/', views.get_user_and_profiles),
    path('saveuserprofile/', views.save_user_profile),
    path('deleteuserprofile/', views.delete_user_profile),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]