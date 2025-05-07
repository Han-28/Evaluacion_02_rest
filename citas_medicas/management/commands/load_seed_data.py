from django.core.management.base import BaseCommand
from citas_medicas.models import Medico, Paciente, HistoriaMedica, Cita

class Command(BaseCommand):
    help = 'Carga los datos de ejemplo (seed data)'

    def handle(self, *args, **kwargs):
        # Médicos
        medico1 = Medico.objects.create(nombre="Dr. Juan Pérez", especialidad="Cardiología", disponibilidad=True)
        medico2 = Medico.objects.create(nombre="Dra. Laura Gómez", especialidad="Pediatría", disponibilidad=True)

        # Pacientes
        paciente1 = Paciente.objects.create(nombre="Carlos Díaz", fecha_nacimiento="1985-06-15")
        paciente2 = Paciente.objects.create(nombre="María Torres", fecha_nacimiento="1990-12-10")

        # Historias médicas
        HistoriaMedica.objects.create(paciente=paciente1, diagnosticos="Hipertensión")
        HistoriaMedica.objects.create(paciente=paciente2, diagnosticos="Asma")

        # Citas
        Cita.objects.create(paciente=paciente1, medico=medico1, fecha="2025-06-15T09:00:00Z", motivo="Chequeo regular")
        Cita.objects.create(paciente=paciente2, medico=medico2, fecha="2025-06-16T10:00:00Z", motivo="Consulta por fiebre")

        self.stdout.write(self.style.SUCCESS('Datos cargados correctamente'))
