# API Gestión de Citas Médicas

API RESTful desarrollada con **Django** y **Django REST Framework** para la gestión de citas médicas.

## Características

- **CRUD completo** para **Médicos**, **Pacientes** y **Citas**.
- **Endpoint de disponibilidad de médicos**: Permite verificar si un médico está disponible.
- **Endpoint de programación de citas**: Permite programar, reprogramar y cancelar citas médicas.
- **Consulta de historial médico**: Permite consultar el historial médico de los pacientes.
  
## Endpoints de la API

### Médicos
- `GET /api/medicos/` - Obtener todos los médicos
- `GET /api/medicos/{id}/` - Obtener un médico específico
- `POST /api/medicos/` - Crear un nuevo médico
- `PUT /api/medicos/{id}/` - Actualizar la información de un médico
- `DELETE /api/medicos/{id}/` - Eliminar un médico

### Pacientes
- `GET /api/pacientes/` - Obtener todos los pacientes
- `POST /api/pacientes/` - Crear un nuevo paciente

### Citas
- `POST /api/citas/programar/` - Programar una nueva cita médica

### Disponibilidad de Médicos
- `GET /api/medicos/{id}/disponibilidad/` - Verificar la disponibilidad de un médico

## Tecnologías

- **Django**: Framework para el desarrollo web.
- **Django REST Framework**: Framework para crear APIs RESTful.
- **SQLite** (por defecto): Base de datos utilizada para este proyecto.
- **Postman**: Herramienta utilizada para realizar y probar las solicitudes a la API.

## Características

- Gestión de **Médicos**, **Pacientes** y **Citas**.
- Verificación de la **disponibilidad de médicos**.
- Programación, reprogramación y cancelación de citas.
- Consulta de **historial médico**.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestion-citas-medicas.git
cd gestion-citas-medicas

