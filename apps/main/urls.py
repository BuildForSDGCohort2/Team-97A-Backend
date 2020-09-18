from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

app_name = "core"

router = DefaultRouter()
router.register('packages/', views.PackageViewset, basename="packages")
router.register('packages/verify/', views.PackageVerificationViewset, basename='packages-verify')
router.register('trackers/', views.TrackerViewSet, basename="trackers")

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
] 
urlpatterns += router.urls
# print(urlpatterns)