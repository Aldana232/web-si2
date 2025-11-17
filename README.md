# Mi Empresa - Sistema de Gestión

Sistema de gestión empresarial con funcionalidades de gestión de clientes, créditos, auditoría y más.

## Estructura del Proyecto

```
web_si2/
├── BackendLinux/          # Django REST API
│   ├── venv/              # Virtual Environment
│   ├── manage.py
│   ├── requirements.txt
│   ├── app_Cliente/       # Módulo de Clientes
│   ├── app_Credito/       # Módulo de Créditos
│   ├── app_Empresa/       # Módulo de Empresa
│   ├── app_User/          # Módulo de Usuarios y Grupos
│   ├── Raiz_Project/      # Configuración principal
│   └── docs/              # Documentación
└── FrontendGrupal/        # React + Vite Frontend
    ├── src/
    │   ├── modules/       # Módulos por funcionalidad
    │   ├── shared/        # Componentes compartidos
    │   └── styles/        # Estilos globales
    └── package.json
```

## Requisitos

- Python 3.14+
- Node.js 16+
- SQLite3

## Setup Backend

```bash
cd BackendLinux

# Crear y activar virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

El backend estará disponible en: http://127.0.0.1:8000

## Setup Frontend

```bash
cd FrontendGrupal

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

El frontend estará disponible en: http://localhost:5173

## API Endpoints Principales

### Usuarios y Grupos
- `GET /api/User/group/` - Listar grupos
- `POST /api/User/group/` - Crear grupo
- `GET /api/User/permission/` - Listar permisos

### Clientes
- `GET /api/Clientes/clientes/` - Listar clientes
- `POST /api/Clientes/clientes/` - Crear cliente
- `GET /api/Clientes/documentacion/` - Documentación de clientes

### Créditos
- `GET /api/Creditos/creditos/` - Listar créditos
- `POST /api/Creditos/creditos/` - Crear crédito
- `GET /api/Creditos/historial/` - Historial de créditos

## Características

- ✅ Autenticación con Token
- ✅ Sistema multitenant (por empresa)
- ✅ Gestión de usuarios y permisos
- ✅ Gestión completa de clientes
- ✅ Sistema de créditos y financiamiento
- ✅ Auditoría de operaciones
- ✅ Dashboard interactivo

## Tecnologías

### Backend
- Django 5.2.7
- Django REST Framework
- SQLite
- drf-spectacular (API docs)

### Frontend
- React 18
- TypeScript
- Vite
- CSS3

## Configuración CORS

El backend está configurado para aceptar requests desde:
- http://localhost:5173
- http://localhost:3000
- http://127.0.0.1:5173
- http://127.0.0.1:3000

## Licencia

Privado

## Autor

Tu Nombre
