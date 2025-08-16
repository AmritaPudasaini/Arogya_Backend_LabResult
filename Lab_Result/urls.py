from django.urls import path
from .views import hospital_list, lab_list, report_list

urlpatterns = [
    path("hospitals/", hospital_list, name="hospital_list"),
    path("labs/", lab_list, name="lab_list"),
    path("reports/", report_list, name="report_list"),
]
