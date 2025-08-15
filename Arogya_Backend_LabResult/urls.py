from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Application.urls')),  # <- changed here
    path('', include('Application.urls')),      # <- added for root
]
