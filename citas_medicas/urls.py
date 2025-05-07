from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, PacienteViewSet, CitaViewSet, HistoriaMedicaViewSet

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'historias', HistoriaMedicaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
