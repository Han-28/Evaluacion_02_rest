from django.db import models

# Modelo Médico
class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    disponibilidad = models.BooleanField(default=True)  # Si está disponible para citas

    def __str__(self):
        return self.nombre

# Modelo Paciente
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# Modelo Historia Médica
class HistoriaMedica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    diagnosticos = models.TextField()

    def __str__(self):
        return f"Historia Médica de {self.paciente.nombre}"

# Modelo Cita
class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con {self.medico.nombre} en {self.fecha}"
