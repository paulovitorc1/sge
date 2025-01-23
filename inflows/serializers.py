from rest_framework import serializers
from inflows.models import Inflows

class InflowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inflows
        fields = '__all__'