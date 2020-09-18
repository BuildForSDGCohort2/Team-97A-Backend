from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('users/', views.UserDetailsViewset, basename="users")

app_name = "accounts"
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

]
urlpatterns += router.urls