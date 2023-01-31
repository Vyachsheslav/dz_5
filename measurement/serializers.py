from rest_framework import serializers

from measurement.models import Sensor,Measurement

# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id','temperature', 'created_at']

class SensorsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Sensor
        fields = ['id','name', 'description']

class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id','name', 'description', 'measurements']

    
