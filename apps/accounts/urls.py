from django.urls import path, include

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register', include('dj_rest_auth.registration.urls')),
]
