from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LabResult
from .serializers import LabResultSerializer

@api_view(['GET'])
def hospital_list(request):
    """
    API endpoint to list hospitals.
    Currently uses hardcoded data.
    """
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
    """
    API endpoint to list lab tests.
    Currently uses hardcoded data.
    """
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
    """
    API endpoint to list lab results (reports) from the database.
    This view uses the LabResult model and serializer to provide dynamic data.
    """
    # Fetch all objects from the LabResult model
    reports = LabResult.objects.all()

    # Serialize the queryset of reports
    serializer = LabResultSerializer(reports, many=True)

    # Return the serialized data as a JSON response
    return Response(serializer.data)

@api_view(['POST'])
def create_lab_result(request):
    """
    API endpoint to create a new lab result.
    """
    serializer = LabResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
