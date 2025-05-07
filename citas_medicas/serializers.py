from rest_framework import serializers
from .models import Medico, Paciente, HistoriaMedica, Cita

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class HistoriaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaMedica
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
