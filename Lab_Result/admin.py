from django.contrib import admin
from .models import LabTest, Hospital, LabReport, LabResultValue

# Register your new models here.
admin.site.register(LabTest)
admin.site.register(Hospital)
admin.site.register(LabReport)
admin.site.register(LabResultValue)