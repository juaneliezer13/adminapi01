# adminapi01

Proyecto reorganizado a Clean Architecture. La implementación principal está en `src/`.

Resumen rápido
- Entrypoint FastAPI: `src.main:app`
- Ejecutar con Docker Compose: `API_PORT=8080 docker-compose up --build`

Qué contiene cada carpeta (explicación fácil)

- `src/domain/`  
  - Qué: Entidades y reglas de negocio puras.  
  - Por qué: Aquí vive la lógica que no depende de frameworks ni infra.  
  - Contenido típico: dataclasses/objetos de dominio, validaciones y business rules.

- `src/application/`  
  - Qué: Casos de uso (orquestación).  
  - Por qué: Coordina llamadas a repositorios, validaciones y políticas.  
  - Contenido típico: funciones o clases `use_cases` que implementan operaciones (ej. `register_user`).

- `src/infrastructure/`  
  - Qué: Implementaciones técnicas concretas.  
  - Por qué: Aislamos DB, repositorios, clientes externos y detalles de implementación.  
  - Contenido típico: SQLAlchemy models, adaptadores/repositories, acceso a DB, configuración y utilidades (`config`, `security`).

- `src/presentation/`  
  - Qué: Interfaz con el mundo (API).  
  - Por qué: Se encarga de recibir requests, validar y devolver respuestas.  
  - Contenido típico: routers/endpoints (controllers), `pydantic` schemas para input/output, manejadores de errores.
    - `src/presentation/api/v1/endpoints/` → routers/controlladores (controllers)
    - `src/presentation/api/v1/api_router.py` → agrega y exporta routers de la versión
    - `src/presentation/schemas/` → pydantic models para la API
    - `src/presentation/common/` → middlewares y manejadores (ej. excepciones)

- Otros archivos importantes
  - `Dockerfile`, `docker-compose.yml`: configuración de contenedores.  
  - `requirements.txt`: dependencias Python.  
  - `.env.example`: variables de entorno necesarias (DB, SECRET_KEY, API_PORT).

Buenas prácticas
- Mantén la lógica de negocio en `domain` y `application` para facilitar testing y reemplazo de infra.  
- Los cambios en `infrastructure` no deberían afectar la API ni los casos de uso si las interfaces se mantienen.

Si quieres, puedo añadir un diagrama simple o un archivo `CONTRIBUTING.md` con convenciones para seguir la arquitectura.

---

## Propuesta: migración a Arquitectura Hexagonal ✅

He añadido un scaffold inicial bajo `src/` con los siguientes conceptos implementados como ejemplo:

- DTOs y `pydantic` schemas en `src/shared/dto/` y `src/presentation/schemas/`. 💡
- Mappers (conversión entre modelos SQLAlchemy y entidades de dominio) en `src/shared/mappers/`. 🔧
- Puertos (interfaces) en `src/ports/` (por ejemplo `UserRepositoryPort`, `AuthServicePort`).
- Adaptadores (implementaciones concretas) en `src/adapters/` (ej. `SQLAlchemyUserRepository`, `JWTAuthAdapter`).
- Carpetas para servicios externos en `src/infrastructure/external_services/` (cliente HTTP como ejemplo).
- Export funcional: servicio y adaptador CSV en `src/application/export/` y `src/adapters/export/`, y endpoint `GET /export/users` como ejemplo.

Cómo está pensado usarlo (rápido):
1. Los endpoints usan los Use Cases en `src/application/use_cases/`.
2. Los Use Cases dependen exclusivamente de puertos (interfaces).
3. Los adaptadores implementan esos puertos y se inyectan desde los endpoints (o desde un contenedor DI en el futuro).

Siguientes pasos que puedo hacer según prefieras:
- Completar tests y ejemplos de integración. ✅
- Implementar todas las operaciones existentes (migrar `/auth/register` y `/auth/login` con tests). ✅
- Agregar un cliente HTTP real en `infrastructure/external_services` y ejemplos de uso.
- Crear `CONTRIBUTING.md` con convenciones y diagrama de carpetas.

Dime qué quieres que haga a continuación y lo implemento. ✨
