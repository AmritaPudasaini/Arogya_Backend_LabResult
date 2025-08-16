from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Lab_Result.urls')), # App name changed
    path('', include('Lab_Result.urls')),      # App name changed
]
