from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

app_name = "core"

router = DefaultRouter()
router.register(r'packages', views.PackageViewset, basename="packages")
router.register(r'trackers', views.TrackerViewSet, basename="trackers")

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
]
urlpatterns += router.urls

# To see all urls
# import pprint
# pprint.pprint(urlpatterns)
