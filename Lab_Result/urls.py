from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LabResultViewSet

router = DefaultRouter()
router.register(r'labresults', LabResultViewSet, basename='labresult')

# The `urlpatterns` should only include patterns for this app
urlpatterns = router.urls