from django.contrib import admin
from .models import LabResult

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'test_name', 'result_value', 'unit', 'date')
    search_fields = ('patient_id', 'test_name')
