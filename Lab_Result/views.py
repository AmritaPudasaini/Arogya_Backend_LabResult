from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hospital_list(request):
    data = [
        {
            "id": "1",
            "date": "01/23/2024",
            "name": "NRL Diagnostics",
            "address": "123 Medical Center Dr",
            "phone": "+1 (555) 123-4567",
            "type": "Diagnostic Center",
        },
        {
            "id": "2",
            "date": "07/16/2023",
            "name": "Teaching Hospital",
            "address": "456 University Ave",
            "phone": "+1 (555) 987-6543",
            "type": "General Hospital",
        },
    ]
    return Response(data)

@api_view(['GET'])
def lab_list(request):
    data = [
        {
            "id": "1",
            "name": "Complete Blood Count",
            "subTests": ["Hemoglobin", "WBC Count", "Platelet Count", "RBC Count"],
            "date": "2024-01-15",
            "status": "Completed",
        }
    ]
    return Response(data)

@api_view(['GET'])
def report_list(request):
    data = [
        {
            "id": "1",
            "testName": "Complete Blood Count",
            "date": "2024-01-15",
            "hospital": "NRL Diagnostics",
            "status": "Ready",
        }
    ]
    return Response(data)
