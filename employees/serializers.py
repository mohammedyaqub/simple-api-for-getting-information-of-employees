from .models import employee
from rest_framework import serializers

class employeeSerializer(serializers.ModelSerializer):
    

    class Meta():
        model=employee
       # fields='all' fields = ('request_id', 'last_seed', 'available_flights')
        fields=('first_name','last_name','employee_id','challenge','done','working','quality_check')