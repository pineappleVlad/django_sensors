from rest_framework import serializers

from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']

    def create(self, validated_data):
        sensor = self.context['sensor']
        measurement = Measurement.objects.create(sensor_id=sensor, **validated_data)
        return measurement
class OneSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

class SensorSerializer(serializers.ModelSerializer):
    sens_id = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'sens_id']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


