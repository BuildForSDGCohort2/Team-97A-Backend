from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


app_name = "accounts"
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

]
