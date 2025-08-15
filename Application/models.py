from django.db import models

class LabResult(models.Model):
    patient_id = models.CharField(max_length=100)
    test_name = models.CharField(max_length=255)
    result_value = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.test_name} - {self.result_value} {self.unit or ''}"
