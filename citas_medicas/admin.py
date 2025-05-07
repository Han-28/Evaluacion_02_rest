from django.contrib import admin
from .models import Medico, Paciente, HistoriaMedica, Cita

# Registrar los modelos en el panel de administración
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(HistoriaMedica)
admin.site.register(Cita)
