from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view),
]

from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Hello from Application app!")
