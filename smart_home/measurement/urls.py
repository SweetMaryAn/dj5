from django.urls import path
from measurement.views import SensorAPIList, SensorAPIUpdate, MeasurementAPIView

urlpatterns = [
    path('sensor/', SensorAPIList.as_view()),
    path('sensor/<pk>/', SensorAPIUpdate.as_view()),
    path('measurement/', MeasurementAPIView.as_view())
]