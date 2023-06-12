from .models import Sensor, Measurement
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import SensorSerializer, MeasurementSerializer, OneSensorSerializer

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = OneSensorSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
