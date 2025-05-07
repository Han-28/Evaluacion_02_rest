from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Medico, Paciente, Cita, HistoriaMedica
from .serializers import MedicoSerializer, PacienteSerializer, CitaSerializer, HistoriaMedicaSerializer

# ViewSet para los Médicos
class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    # Endpoint para verificar la disponibilidad de un médico
    @action(detail=True, methods=['get'])
    def disponibilidad(self, request, pk=None):
        medico = self.get_object()
        return Response({"disponible": medico.disponibilidad})

# ViewSet para los Pacientes
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

# ViewSet para las Citas
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    # Endpoint para programar una cita
    @action(detail=False, methods=['post'])
    def programar(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cita = serializer.save()
            return Response(CitaSerializer(cita).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Endpoint para reprogramar una cita
    @action(detail=True, methods=['put'])
    def reprogramar(self, request, pk=None):
        cita = self.get_object()
        serializer = self.get_serializer(cita, data=request.data, partial=True)
        if serializer.is_valid():
            cita = serializer.save()
            return Response(CitaSerializer(cita).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Endpoint para cancelar una cita
    @action(detail=True, methods=['delete'])
    def cancelar(self, request, pk=None):
        cita = self.get_object()
        cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ViewSet para las Historias Médicas
class HistoriaMedicaViewSet(viewsets.ModelViewSet):
    queryset = HistoriaMedica.objects.all()
    serializer_class = HistoriaMedicaSerializer

    # Endpoint para consultar historial médico
    @action(detail=True, methods=['get'])
    def consultar_historial(self, request, pk=None):
        historia = self.get_object()
        return Response(HistoriaMedicaSerializer(historia).data)
