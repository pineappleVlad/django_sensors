from django.urls import path

from measurement.views import SensorView, OneSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
