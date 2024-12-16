# Prueba Técnica Crecer Lab

Este documento describe el proceso de configuración, ejecución y pruebas del proyecto, además de señalar los puntos faltantes y pendientes para completar esta prueba técnica.

## Requisitos previos

Antes de comenzar, asegúrese de contar con los siguientes elementos instalados y configurados:

1. **Python** (versión 3.13 o superior).
2. **Poetry**: Una herramienta para la gestión de dependencias y el entorno virtual.
3. **Redis**: Necesario para Celery como broker de mensajes.

## Configuración del proyecto

Siga los pasos a continuación para configurar el entorno del proyecto:

1. Clone este repositorio en su máquina local:

   ```bash
   git clone https://github.com/OmarNunezG/PruebaTecnica-CrecerLab.git
   cd PruebaTecnica-CrecerLab
   ```

2. Instale las dependencias del proyecto usando Poetry:

   ```bash
   poetry install
   ```

3. Cree un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

   ```env
   CELERY_BROKER_URL=redis://redis:6379/0
   CELERY_RESULT_BACKEND=redis://redis:6379/0
   ```

4. Active el entorno virtual de Poetry:

   ```bash
   poetry shell
   ```

5. Ejecute el docker-compose:
   ```bash
   docker compose up --build
   ```

## Ejecución de pruebas

Para ejecutar las pruebas unitarias del proyecto, use el siguiente comando:

```bash
pytest
```

Nota: Actualmente, las pruebas no se ejecutan correctamente debido a un problema con Celery y Redis. Consulte la sección **Puntos faltantes** para más detalles.

## Documentación de la API

La documentación interactiva de la API está disponible en los siguientes enlaces una vez que el servidor esté en ejecución:

- [Swagger](http://localhost:8000/documentation/swagger)
- [Redoc](http://localhost:8000/documentation/redoc)

## Puntos faltantes

1. **Pruebas:**

   - **Motivo 1:** Tiempo.
   - **Motivo 2:** Se produce un error al intentar ejecutar pruebas relacionadas con Celery y Redis debido a problemas de conexión.
   - **Solución pendiente:** Investigar y resolver los problemas de configuración de Celery y Redis para garantizar que las pruebas puedan ejecutarse sin errores. Otra opción podría ser comunicarme con ustedes directamente, y coordinar una reunión para recibir ayuda/soporte para corregir el problema.

2. **Punto 2.3:**
   - **Motivo:** El enunciado de esta tarea no quedó claro.
   - **Acción pendiente:** Solicitar aclaraciones sobre el punto 2.3 para poder completarlo.
