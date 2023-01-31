# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor,Measurement
from .serializers import SensorSerializer, SensorsSerializer, MeasurementSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()    
    serializer_class = SensorsSerializer
    

    def POST(self, request):
        
        return Response({'status': 'OK'})
    

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        return Response({'status': 'OK'})   

 

class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()    
    serializer_class = MeasurementSerializer
    

    def POST(self, request):
        
        return Response({'status': 'OK'})

    