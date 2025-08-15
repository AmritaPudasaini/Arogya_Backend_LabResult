from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Report(APIView):
    def get(self, request):
        return Response({"message": "Lab Report"}, status=status.HTTP_200_OK)

def test_view(request):
    return JsonResponse({"message": "Test View is working!"})