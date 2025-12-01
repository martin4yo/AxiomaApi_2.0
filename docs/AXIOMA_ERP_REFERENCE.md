# AXIOMA ERP - Documento de Referencia Técnica

**Fecha de creación**: 2025-12-01
**Propósito**: Guía técnica completa del sistema ERP Axioma para desarrollo continuo

---

## 1. ARQUITECTURA GENERAL DEL SISTEMA

### Visión General
Axioma ERP es un sistema empresarial multi-tenant con arquitectura de microservicios que separa:
- **Gestión de usuarios y autenticación** (Node.js + PostgreSQL)
- **Datos maestros comerciales** (Django + MySQL)
- **Interfaz de usuario** (React + TypeScript)

### Repositorios del Proyecto

```
C:\Ex drive\AXIOMA\ERP\
├── project/                    # Frontend + Backend Node.js
│   ├── Axioma-FE/             # React Frontend
│   └── Axioma-BE/             # Express Backend + PostgreSQL
└── AxiomaApi_2.0/             # Django Backend + MySQL
```

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│              FRONTEND (React + TypeScript)              │
│              http://localhost:5173                      │
│              Tecnologías: Vite, Tailwind, shadcn/ui    │
└────────────┬──────────────────────┬─────────────────────┘
             │                      │
             │ (JWT Auth)          │ (Token Auth)
             ↓                      ↓
┌────────────────────────┐  ┌──────────────────────────┐
│  NODE.JS BACKEND       │  │  DJANGO REST API         │
│  http://localhost:8800 │  │  http://localhost:8000   │
│  Express + Prisma      │  │  Django + DRF            │
├────────────────────────┤  ├──────────────────────────┤
│  • Autenticación JWT   │  │  • Datos maestros        │
│  • Gestión de usuarios │  │  • Productos             │
│  • Multi-tenant        │  │  • Entidades comerciales │
│  • Roles y permisos    │  │  • Impuestos             │
│  • Clientes/Contactos  │  │  • Contabilidad          │
│  • OAuth Google        │  │  • API RESTful (47+ EP)  │
└───────────┬────────────┘  └──────────┬───────────────┘
            │                          │
            ↓                          ↓
┌────────────────────────┐  ┌──────────────────────────┐
│  PostgreSQL            │  │  MySQL 8.0+              │
│  axiomadb              │  │  axiomaconnect           │
│  • Users               │  │  • 78 tablas             │
│  • Tenants             │  │  • 5 dominios            │
│  • Roles               │  │  • Multi-tenant          │
│  • Clients             │  │  • Audit trail           │
│  • Contacts            │  │  • Soft deletes          │
└────────────────────────┘  └──────────────────────────┘
```

---

## 2. FRONTEND - Axioma-FE (React + TypeScript)

### Stack Tecnológico

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| React | 18.2.0 | Framework UI |
| TypeScript | 5.2.2 | Tipado estático |
| Vite | 5.1.0 | Build tool |
| React Router | v6 | Navegación |
| Tailwind CSS | 3.4.1 | Estilos |
| shadcn/ui | 0.8.0 | Componentes UI |
| React Hook Form | 7.51.1 | Gestión de formularios |
| Zod | 3.22.4 | Validación |
| Axios | 1.6.7 | Cliente HTTP |
| i18next | 23.11.1 | Internacionalización |
| date-fns | 3.6.0 | Manejo de fechas |
| next-themes | - | Dark/Light mode |

### Estructura de Directorios

```
Axioma-FE/
├── src/
│   ├── api/                    # Configuración de Axios
│   │   ├── axios.ts           # Instancia base
│   │   └── axiosAxioma.ts     # Config específica Axioma
│   ├── pages/                  # Páginas principales
│   │   ├── login.tsx
│   │   ├── users.tsx
│   │   ├── entities.tsx
│   │   ├── products.tsx
│   │   ├── profile.tsx
│   │   ├── google-auth.tsx
│   │   ├── register-from-link.tsx
│   │   └── reset-password.tsx
│   ├── components/             # Componentes reutilizables
│   │   ├── ui/                # shadcn/ui components
│   │   ├── header.tsx
│   │   ├── sidebar/
│   │   ├── users/
│   │   ├── entities/          # Gestión de entidades
│   │   ├── productos/
│   │   └── edit-panel/        # Paneles de edición
│   ├── context/               # React Context
│   │   ├── auth-context.tsx
│   │   └── tenant-context.tsx
│   ├── hooks/                 # Custom hooks
│   │   ├── use-auth.tsx
│   │   ├── use-tenant.tsx
│   │   ├── use-role-check.tsx
│   │   ├── use-logout.tsx
│   │   └── use-axios-private.tsx
│   ├── services/              # API services
│   │   ├── login-service.tsx
│   │   └── register-service.tsx
│   ├── types/                 # TypeScript types
│   ├── lib/                   # Utilidades
│   └── assets/locales/        # Traducciones (en, es)
├── public/
├── index.html
├── vite.config.ts
├── tailwind.config.js
├── tsconfig.json
└── package.json
```

### Variables de Entorno

```bash
# .env
VITE_REACT_APP_API_BASE_ENDPOINT=http://localhost:8800/api
VITE_AXIOMA_CLOUD_API=http://localhost:8000/api
VITE_AXIOMA_ACCESS_TOKEN=Token ...
```

### Páginas Principales

1. **Login** (`/login`) - Autenticación con JWT y OAuth Google
2. **Users** (`/users`) - Gestión de usuarios (admin)
3. **Entities** (`/entities`) - Gestión de entidades comerciales
4. **Products** (`/products`) - Catálogo de productos
5. **Profile** (`/profile`) - Perfil del usuario

### Flujo de Autenticación

```
1. Usuario ingresa credenciales
   ↓
2. POST /api/auth/login (Node.js Backend)
   ↓
3. Backend verifica y retorna JWT + RefreshToken
   ↓
4. RefreshToken → HttpOnly Cookie
   AccessToken → Context en memoria
   ↓
5. Todas las peticiones incluyen: Authorization: Bearer {token}
   ↓
6. Token se refresca automáticamente antes de expirar (7200s)
```

### Comandos de Desarrollo

```bash
cd "C:\Ex drive\AXIOMA\ERP\project\Axioma-FE"
npm run dev      # Puerto 5173
npm run build    # Compilar para producción
npm run lint     # ESLint
```

---

## 3. BACKEND NODE.JS - Axioma-BE (Express + PostgreSQL)

### Stack Tecnológico

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| Node.js | ES modules | Runtime |
| Express.js | 4.18.2 | Framework web |
| Prisma | 5.15.0 | ORM |
| PostgreSQL | - | Base de datos |
| JWT | 9.0.0 | Autenticación |
| bcrypt | 5.1.0 | Hash de contraseñas |
| Nodemailer | 6.9.9 | Envío de emails |
| Google Auth | 9.10.0 | OAuth 2.0 |
| node-cron | 3.0.3 | Tareas programadas |

### Estructura de Directorios

```
Axioma-BE/
├── config/                     # Configuración
│   ├── allowedOrigins.js      # Lista CORS
│   ├── corsOptions.js
│   ├── nodemailer.config.js
│   └── constants/
│       ├── roles.js           # SUPER_ADMIN=3, ADMIN=1, USER=2
│       └── tenants.js
├── controllers/                # Lógica de controladores
│   ├── auth.js                # Autenticación
│   ├── user.js                # Usuarios
│   ├── client.js              # Clientes
│   ├── contact.js             # Contactos
│   ├── group.js
│   ├── role.js
│   ├── tenant.js
│   ├── request.js
│   ├── bulk.js
│   └── oauth.js
├── routes/                     # Rutas API
│   ├── auth.js                # /api/auth
│   ├── users.js               # /api/users
│   ├── clients.js             # /api/clients
│   ├── contacts.js            # /api/contacts
│   ├── groups.js
│   ├── roles.js
│   ├── tenants.js
│   ├── request.js
│   ├── bulks.js
│   └── oauth.js
├── services/                   # Lógica de negocio
│   ├── authService.js
│   ├── usersService.js
│   ├── clientsService.js
│   ├── contactsService.js
│   ├── groupsService.js
│   ├── rolesService.js
│   ├── tenantsService.js
│   └── bulkService.js
├── lib/
│   ├── db.js                  # Cliente Prisma (soft-delete)
│   ├── utils/                 # Utilidades específicas
│   └── validations/           # Validaciones de entrada
├── middlewares/
│   ├── verifyToken.js         # Verificación JWT
│   ├── verifyRoles.js         # RBAC
│   ├── credentials.js
│   ├── error-handler.js
│   └── not-found.js
├── errors/                     # Errores personalizados
│   ├── custom-api.js
│   ├── bad-request.js         # 400
│   ├── unauthenticated.js     # 401
│   ├── forbidden.js           # 403
│   ├── not-found.js           # 404
│   ├── conflict.js            # 409
│   └── internal-error.js      # 500
├── prisma/
│   ├── schema.prisma          # Modelos de datos
│   └── migrations/
├── index.js                    # Punto de entrada
├── package.json
└── .env
```

### Variables de Entorno

```bash
# .env
DATABASE_URL=postgresql://postgres:Q27G4B98@localhost:5432/axiomadb
JWT=<secret>
JWT_LIFETIME=7200s
REFRESH_JWT=<secret>
REFRESH_JWT_LIFETIME=20d
EMAIL_USER=...
EMAIL_PASS=...
ENCRYPTION_KEY=...
IV_HEX=...
CLIENT_ID=...                  # Google OAuth
CLIENT_SECRET=...
GOOGLE_REDIRECT_URL=...
FRONTEND_URL=http://localhost:5173
BACKEND_URL=http://localhost:8800
```

### Principales Endpoints (Puerto 8800)

#### Autenticación (`/api/auth`)
```
POST   /login                        # Login usuario
POST   /login-to-tenant              # Login a tenant específico
POST   /register                     # Registro
POST   /register/send-link           # Enviar link de registro
GET    /register/:encodedData        # Verificar datos de registro
GET    /refresh/:id                  # Refrescar token
POST   /send-reset-password-link     # Solicitar reset password
GET    /verify-reset-password-link/:id/:token
PUT    /change-password/:id
PUT    /change-password-from-profile
GET    /logout
```

#### Usuarios (`/api/users`) - Protegido con roles
```
GET    /                             # Listar usuarios (admin)
GET    /:id                          # Obtener usuario
GET    /:id/get-roles-groups         # Obtener roles y grupos (admin)
PUT    /:id                          # Actualizar usuario (self)
PUT    /:id/update-groups            # Actualizar grupos (admin)
PUT    /:id/update-roles             # Actualizar roles (admin)
PUT    /:id/status                   # Actualizar estado (admin)
DELETE /:id                          # Eliminar usuario
```

#### Clientes (`/api/clients`) - Admin only
```
POST   /                             # Crear cliente
GET    /                             # Listar clientes
GET    /:id                          # Obtener cliente
PUT    /:id                          # Actualizar cliente
DELETE /:id                          # Eliminar cliente
```

#### Otros Endpoints
- `/api/tenants` - Gestión multi-tenant
- `/api/roles` - Gestión de roles (super admin)
- `/api/contacts` - Gestión de contactos (admin)
- `/api/groups` - Gestión de grupos (admin)
- `/api/request` - Manejo de solicitudes
- `/api/oauth` - Integración OAuth
- `/api/bulk` - Operaciones masivas (admin)

### Modelo de Datos Prisma (PostgreSQL)

```prisma
// Principales modelos

User
├── id, email, username, password
├── client_id (FK → Client)
├── Profile (1:1)
├── refresh_token, reset_password_token
├── registered_by_google, is_profile_completed
└── Relations: TenantUserRole, TenantUserGroup, UserTenant

Tenant
├── id, name, logo_url, logo_url_dark
├── url_identifier (unique)
├── is_active
└── Relations: Client, Contact, User, Role, Group

Role
├── id, role (unique)
├── is_active
└── Relations: RoleTranslation, TenantUserRole

Client
├── id, name, celocity_percentage
├── tenant_id (FK)
├── is_active
└── Relations: User

Contact
├── id, email (unique), phone, name, last_name
├── tenant_id (FK)
└── Relations: Tenant

// Roles predefinidos (constants/roles.js)
SUPER_ADMIN = 3
ADMIN = 1
USER = 2
```

### Seguridad y Autenticación

- **JWT Access Token**: 7200 segundos (2 horas)
- **Refresh Token**: 20 días (HttpOnly cookie)
- **Password Hashing**: bcrypt con salt rounds
- **Soft Delete**: Todos los modelos con campo `deleted_at`
- **RBAC**: 3 niveles (Super Admin, Admin, User)
- **CORS**: Whitelist configurada en `allowedOrigins.js`

### Comandos de Desarrollo

```bash
cd "C:\Ex drive\AXIOMA\ERP\project\Axioma-BE"
npm run dev              # Inicia servidor puerto 8800
npx prisma studio        # Interfaz visual de BD
npx prisma migrate dev   # Crear migración
npx prisma generate      # Generar cliente Prisma
```

---

## 4. BACKEND DJANGO - AxiomaApi_2.0 (Python + MySQL)

### Stack Tecnológico

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| Python | 3.12 | Lenguaje |
| Django | 5.1.2 | Framework web |
| Django REST Framework | 3.15.2 | API REST |
| MySQL | 8.0+ | Base de datos |
| mysqlclient | 2.2.5 | Driver MySQL |
| django-filter | 24.3 | Filtros API |
| django-cors-headers | 4.6.0 | CORS |
| django-redis | 5.4.0 | Cache Redis |
| drf-spectacular | 0.27.2 | Documentación OpenAPI |
| django-jazzmin | 3.0.1 | Admin moderno |
| django-silk | 5.1.0 | Profiling |

### Estructura de Directorios

```
AxiomaApi_2.0/
├── AxiomaConnect/              # Configuración Django
│   ├── settings.py            # Configuración principal
│   ├── urls.py                # Rutas raíz
│   ├── middlewares.py         # Middlewares custom
│   ├── wsgi.py
│   └── asgi.py
├── MasterModels/               # 78 modelos de datos
│   ├── modelos_general/       # 18 modelos generales
│   │   ├── persona.py         # Usuario/persona
│   │   ├── pais.py
│   │   ├── provincia.py
│   │   ├── moneda.py
│   │   ├── idioma.py
│   │   ├── rol.py
│   │   └── ...
│   ├── modelos_producto/      # 12 modelos de productos
│   │   ├── producto.py        # Producto principal
│   │   ├── tipoproducto.py
│   │   ├── precio.py
│   │   ├── listaprecio.py
│   │   └── ...
│   ├── modelos_entidad/       # 9 modelos de entidades
│   │   ├── entidad.py         # Entidad comercial
│   │   ├── contactoentidad.py
│   │   ├── direccionentidad.py
│   │   └── ...
│   ├── modelos_impuestos/     # 9 modelos de impuestos
│   │   ├── impuesto.py
│   │   ├── tipoimpuesto.py
│   │   └── ...
│   ├── modelos_contabilidad/  # 2 modelos contables
│   │   ├── plancuenta.py
│   │   └── tipoajuste.py
│   ├── universal.py           # Modelos base abstractos
│   ├── paginators.py          # Paginación custom
│   ├── filters.py             # Sistema de filtros
│   └── migrations/
├── MasterSerializers/          # 78 serializers
│   ├── serializers_general/
│   ├── serializers_producto/
│   ├── serializers_entidad/
│   ├── serializers_impuestos/
│   └── serializers_contabilidad/
├── MasterViewSets/             # 79 viewsets
│   ├── api.py                 # GenericModelViewSet base
│   ├── urls.py                # Rutas API
│   ├── versioning.py          # Versionado API
│   ├── viewsets_auth/
│   ├── viewsets_general/
│   ├── viewsets_producto/
│   ├── viewsets_entidad/
│   ├── viewsets_impuestos/
│   └── viewsets_contabilidad/
├── tests/                      # Suite de tests
│   ├── test_api.py
│   ├── test_models.py
│   └── test_middlewares.py
├── static/ & staticfiles/
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

### Variables de Entorno

```bash
# .env
SECRET_KEY=<very-secure-key>
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,erp.axiomacloud.com

DB_NAME=axiomaconnect
DB_USER=<db_user>
DB_PASSWORD=<secure_password>
DB_HOST=localhost
DB_PORT=3306

REDIS_URL=redis://localhost:6379/0
```

### Endpoints API (Puerto 8000)

La API está organizada en 5 dominios con versionado:

#### Estructura de URLs
```
/api/general/*          # Sin versión (legacy)
/api/v1/general/*       # Versión 1 (actual)
/api/v2/general/*       # Versión 2 (futuro)
```

#### General (18 endpoints)
```
/api/general/persona            # Usuarios/personas
/api/general/pais               # Países
/api/general/provincia          # Provincias
/api/general/codigopostal       # Códigos postales
/api/general/rol                # Roles
/api/general/modulo             # Módulos del sistema
/api/general/formapago          # Formas de pago
/api/general/moneda             # Monedas
/api/general/idioma             # Idiomas
/api/general/sector             # Sectores
... (8 endpoints más)
```

#### Productos (12 endpoints)
```
/api/productos/producto         # Productos
/api/productos/tipoproducto     # Tipos de producto
/api/productos/precio           # Precios
/api/productos/listaprecios     # Listas de precios
/api/productos/atributo         # Atributos
/api/productos/claseproducto    # Clasificaciones
... (6 endpoints más)
```

#### Entidades (13 endpoints)
```
/api/entidades/entidad                      # Entidades comerciales
/api/entidades/contactoentidad              # Contactos
/api/entidades/direccionentidad             # Direcciones
/api/entidades/datosfiscalesentidad         # Datos fiscales
/api/entidades/condicioncrediticiaentidad   # Condiciones crédito
/api/entidades/ejecutivoentidad             # Ejecutivos
/api/entidades/zona                         # Zonas
... (6 endpoints más)
```

#### Impuestos (10 endpoints)
```
/api/impuestos/impuesto         # Impuestos
/api/impuestos/tipoimpuesto     # Tipos de impuesto
/api/impuestos/alicuotaimpuesto # Alícuotas
/api/impuestos/tipocomprobante  # Tipos de comprobante
... (6 endpoints más)
```

#### Contabilidad (2 endpoints)
```
/api/contabilidad/plancuentas   # Plan de cuentas
/api/contabilidad/tipoajuste    # Tipos de ajuste
```

#### Autenticación
```
POST /api/token/                # Generar token
GET  /api/auth/validate/        # Validar usuario
POST /api/auth/validate/        # Validar usuario (JSON)
GET  /api/version/              # Versión de API
```

#### Documentación
```
/api/docs/                      # Swagger UI
/api/redoc/                     # ReDoc
/api/schema/                    # Schema OpenAPI (JSON)
/silk/                          # Profiling y monitoring
/admin/                         # Django Admin (Jazzmin)
```

### Operaciones CRUD Estándar

Todos los endpoints soportan:
```
GET    /:id/     # Obtener registro único
GET    /         # Listar todos (con paginación, filtros, ordenamiento)
POST   /         # Crear nuevo registro
PUT    /:id/     # Actualizar completo
PATCH  /:id/     # Actualizar parcial
DELETE /:id/     # Eliminar registro
OPTIONS /        # Preflight CORS
```

### Modelos Base Abstractos

```python
# universal.py

class AuditModel(models.Model):
    """Auditoría automática"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disabled = models.BooleanField(default=False)  # Soft delete
    user_id = models.ForeignKey('Persona', ...)

    class Meta:
        abstract = True

class TenantModel(models.Model):
    """Soporte multi-tenant"""
    tenant_id = models.BigIntegerField()

    def clean(self):
        if self.tenant_id <= 0:
            raise ValidationError("tenant_id debe ser mayor a 0")

    class Meta:
        abstract = True
```

Todos los modelos de negocio heredan de `AuditModel` y `TenantModel`.

### Middlewares Custom

1. **LogRequestMiddleware**: Log de todas las peticiones
2. **TenantValidationMiddleware**: Valida `tenant_id` en operaciones
3. **DynamicCORSHeadersMiddleware**: CORS dinámico para localhost
4. **AddCOOPHeaderMiddleware**: Headers de seguridad

### Paginación

```python
class CustomPagination(PageNumberPagination):
    page_size = 10              # Por defecto 10 registros
    max_page_size = 100         # Máximo 100 registros
    page_size_query_param = 'page_size'
```

### Filtros Dinámicos

Cada endpoint soporta:
- Filtros por cualquier campo del modelo
- Ordenamiento: `?ordering=campo` o `?ordering=-campo`
- Búsqueda: Según campos definidos en cada viewset

### Comandos de Desarrollo

```bash
cd "C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0"

# Servidor de desarrollo
python manage.py runserver       # Puerto 8000

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Tests
python manage.py test tests/

# Crear superusuario
python manage.py createsuperuser

# Shell interactivo
python manage.py shell

# Verificar configuración
python manage.py check
```

---

## 5. INTEGRACIÓN ENTRE SISTEMAS

### Flujo de Datos Completo

```
┌──────────────────────────────────────────────────────────────┐
│                    Usuario en Frontend                        │
│                    http://localhost:5173                      │
└────────────┬────────────────────────┬────────────────────────┘
             │                        │
   (1) Auth & Users          (2) Master Data
             ↓                        ↓
┌────────────────────────┐  ┌────────────────────────────────┐
│  Node.js Backend       │  │  Django Backend                │
│  localhost:8800        │  │  localhost:8000                │
│                        │  │                                │
│  JWT: Bearer token     │  │  Token: Token xxxxx            │
│  Cookie: refresh_token │  │  Header: X-Tenant-ID           │
└────────────┬───────────┘  └────────────┬───────────────────┘
             │                           │
             ↓                           ↓
┌────────────────────────┐  ┌────────────────────────────────┐
│  PostgreSQL            │  │  MySQL                         │
│  axiomadb              │  │  axiomaconnect                 │
│                        │  │                                │
│  Users, Tenants        │  │  Productos, Entidades          │
│  Roles, Clients        │  │  Impuestos, Contabilidad       │
│  Contacts              │  │  78 tablas                     │
└────────────────────────┘  └────────────────────────────────┘
```

### Escenarios de Integración

#### Escenario 1: Login de Usuario
```
1. Frontend → POST /api/auth/login (Node.js)
2. Node.js valida en PostgreSQL
3. Node.js retorna JWT + RefreshToken
4. Frontend almacena tokens
5. Frontend puede ahora acceder a ambos backends
```

#### Escenario 2: Gestión de Productos
```
1. Frontend → GET /api/productos/producto (Django)
2. Header: Authorization: Token xxxxx
3. Header: X-Tenant-ID: 1
4. Django consulta MySQL
5. Django retorna lista de productos con paginación
```

#### Escenario 3: Crear Entidad Comercial
```
1. Usuario autenticado obtiene tenant_id del contexto
2. Frontend → POST /api/entidades/entidad (Django)
3. Body incluye tenant_id y datos de la entidad
4. TenantValidationMiddleware valida tenant_id
5. Django crea registro en MySQL
6. Respuesta incluye audit trail (created_at, user_id)
```

### CORS Configuration

#### Node.js Backend (allowedOrigins.js)
```javascript
const allowedOrigins = [
  'http://localhost:5173',
  'http://localhost:5174',
  'http://localhost:5175',
  'https://rockingproduct.tech',
  'https://www.rockingproduct.tech',
  'https://axiomacloud.com',
  'https://www.axiomacloud.com'
];
```

#### Django Backend (settings.py)
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5175",
    "https://erp.axiomacloud.com",
]
# + DynamicCORSHeadersMiddleware para localhost:*
```

---

## 6. MULTI-TENANT ARCHITECTURE

### Concepto
Ambos backends soportan multi-tenant, permitiendo que múltiples organizaciones usen la misma instancia.

### Implementación en Node.js (PostgreSQL)

```javascript
// Tenant model con relaciones
model Tenant {
  id              Int      @id @default(autoincrement())
  name            String
  url_identifier  String   @unique
  logo_url        String?
  is_active       Boolean  @default(true)

  // Relaciones
  clients         Client[]
  contacts        Contact[]
  users           UserTenant[]
  roles           TenantUserRole[]
  groups          TenantUserGroup[]
}

// Los usuarios pueden pertenecer a múltiples tenants
model UserTenant {
  user_id   Int
  tenant_id Int
  user      User   @relation(...)
  tenant    Tenant @relation(...)

  @@unique([user_id, tenant_id])
}
```

### Implementación en Django (MySQL)

```python
# Todos los modelos de negocio incluyen:
class Producto(AuditModel, TenantModel):
    tenant_id = models.BigIntegerField()
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)

    class Meta:
        unique_together = [['tenant_id', 'codigo']]  # Único por tenant
```

### Validación de Tenant

**Node.js**: Verificado en contexto de autenticación
**Django**: Middleware `TenantValidationMiddleware` valida en cada request

```python
# TenantValidationMiddleware
if request.method in ['POST', 'PUT', 'PATCH']:
    tenant_id = request.data.get('tenant_id') or \
                request.META.get('HTTP_X_TENANT_ID')
    if not tenant_id:
        return JsonResponse({'error': 'tenant_id requerido'}, status=400)
```

---

## 7. SEGURIDAD Y AUTENTICACIÓN

### Node.js Backend

**Estrategia**: JWT con Refresh Token

```javascript
// Token de acceso
{
  "userId": 123,
  "email": "user@example.com",
  "tenantId": 1,
  "roles": [1, 2],
  "exp": 1234567890  // 7200 segundos (2 horas)
}

// Refresh token (HttpOnly cookie)
{
  "userId": 123,
  "exp": 1234567890  // 20 días
}
```

**Middlewares de Seguridad**:
- `verifyToken.js`: Valida JWT en header Authorization
- `verifyRoles.js`: RBAC - verifica roles requeridos
- `credentials.js`: Manejo de credenciales CORS

**Roles**:
```javascript
// constants/roles.js
SUPER_ADMIN = 3  // Acceso total
ADMIN = 1        // Gestión operacional
USER = 2         // Acceso básico
```

### Django Backend

**Estrategia**: Token Authentication (DRF)

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

**Obtención de Token**:
```bash
POST /api/token/
{
  "username": "usuario",
  "password": "contraseña"
}

Response:
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Uso**:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Mejores Prácticas Aplicadas

1. **Passwords**: Hashing con bcrypt (Node.js) y PBKDF2 (Django)
2. **Tokens**: No se almacenan en localStorage (solo memoria y cookies HttpOnly)
3. **HTTPS**: Forzado en producción
4. **CORS**: Whitelist estricta
5. **Soft Delete**: No se eliminan registros físicamente
6. **Audit Trail**: Todas las operaciones registradas con timestamp y user_id
7. **Environment Variables**: Secrets nunca en código

---

## 8. GESTIÓN DE ERRORES

### Node.js - Custom Error Classes

```javascript
// errors/
BadRequestError      // 400 - Petición inválida
UnauthenticatedError // 401 - No autenticado
ForbiddenError       // 403 - Sin permisos
NotFoundError        // 404 - Recurso no encontrado
ConflictError        // 409 - Conflicto (ej: duplicado)
InternalError        // 500 - Error interno

// Middleware error-handler.js
{
  "error": {
    "message": "Descripción del error",
    "statusCode": 400
  }
}
```

### Django - Standard DRF Errors

```python
# Response format
{
  "detail": "Error message",
  "field_name": ["Error específico del campo"]
}

# Status codes estándar
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Internal Server Error
```

---

## 9. TESTING

### Node.js Backend
Actualmente no hay suite de tests definida. **Pendiente de implementar**.

### Django Backend

```bash
# tests/
test_api.py          # Tests de endpoints
test_models.py       # Tests de modelos
test_middlewares.py  # Tests de middlewares

# Ejecutar tests
python manage.py test tests/
python manage.py test tests.test_api
```

---

## 10. DEPLOYMENT Y PRODUCCIÓN

### Entornos

| Entorno | Frontend | Node.js Backend | Django Backend |
|---------|----------|-----------------|----------------|
| **Development** | localhost:5173 | localhost:8800 | localhost:8000 |
| **Production** | [TBD] | rockingproduct.tech | erp.axiomacloud.com |

### Configuraciones de Producción

#### Frontend (Vite)
```bash
npm run build
# Output: dist/
# Servir con Nginx o similar
```

#### Node.js Backend
```bash
# Usar PM2 o similar
npm run start
# Puerto: 8800
# Reverse proxy con Nginx
```

#### Django Backend
```bash
# Gunicorn + Nginx
gunicorn AxiomaConnect.wsgi:application --bind 0.0.0.0:8000
# Collectstatic para archivos estáticos
python manage.py collectstatic --noinput
```

### Variables de Entorno Críticas

**NUNCA commitear:**
- `SECRET_KEY` (Django)
- `JWT` y `REFRESH_JWT` (Node.js)
- `DATABASE_URL` y credenciales de DB
- `EMAIL_USER` y `EMAIL_PASS`
- `CLIENT_ID` y `CLIENT_SECRET` (Google OAuth)
- Tokens de API

### Checklist de Seguridad Pre-Producción

- [ ] `DEBUG=False` en Django
- [ ] `SECRET_KEY` fuerte y único
- [ ] `ALLOWED_HOSTS` configurado correctamente
- [ ] HTTPS habilitado
- [ ] CORS restrictivo (no usar `*`)
- [ ] Rate limiting implementado
- [ ] Logs configurados
- [ ] Backups de base de datos automatizados
- [ ] Variables de entorno en servidor (no en código)
- [ ] Certificados SSL válidos

---

## 11. MONITOREO Y LOGGING

### Node.js Backend
Actualmente no hay sistema de logging estructurado. **Pendiente de implementar**.

**Recomendaciones**:
- Winston o Pino para logging
- Morgan para HTTP request logging
- Sentry para error tracking

### Django Backend

```python
# settings.py - Logging configurado
LOGGING = {
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/YYYYMMDD.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 7,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

**Profiling con Django Silk**:
- URL: `http://localhost:8000/silk/`
- Monitorea performance de queries
- Identifica cuellos de botella
- Python profiling opcional

---

## 12. PRÓXIMOS PASOS Y MEJORAS

### Tareas Pendientes Identificadas

1. **Testing**:
   - [ ] Implementar suite de tests en Node.js backend
   - [ ] Aumentar cobertura en Django backend
   - [ ] Tests end-to-end (E2E) con Playwright o Cypress

2. **Documentación**:
   - [ ] Swagger/OpenAPI para Node.js backend
   - [x] Swagger implementado en Django (drf-spectacular)
   - [ ] Guías de usuario final

3. **Performance**:
   - [ ] Implementar Redis cache en Node.js
   - [x] Redis configurado en Django (pendiente usar extensivamente)
   - [ ] Query optimization en ambos backends
   - [ ] CDN para assets estáticos

4. **Seguridad**:
   - [ ] Rate limiting en ambos APIs
   - [ ] IP whitelisting para endpoints sensibles
   - [ ] 2FA (Two-Factor Authentication)
   - [ ] Auditoría de seguridad completa

5. **Infraestructura**:
   - [ ] CI/CD pipelines
   - [ ] Docker containerization
   - [ ] Kubernetes para orchestration (si es necesario)
   - [ ] Monitoreo con Prometheus + Grafana

6. **Features**:
   - [ ] WebSockets para notificaciones en tiempo real
   - [ ] Sistema de notificaciones por email más robusto
   - [ ] Exportación de reportes (PDF, Excel)
   - [ ] Dashboard analytics
   - [ ] Mobile app (React Native)

---

## 13. COMANDOS RÁPIDOS DE REFERENCIA

### Levantar el Stack Completo

```bash
# Terminal 1: Frontend
cd "C:\Ex drive\AXIOMA\ERP\project\Axioma-FE"
npm run dev

# Terminal 2: Node.js Backend
cd "C:\Ex drive\AXIOMA\ERP\project\Axioma-BE"
npm run dev

# Terminal 3: Django Backend
cd "C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0"
python manage.py runserver
```

### URLs de Acceso Rápido

```
Frontend:           http://localhost:5173
Node.js API:        http://localhost:8800/api
Django API:         http://localhost:8000/api
Django Admin:       http://localhost:8000/admin
Django API Docs:    http://localhost:8000/api/docs/
Django Profiling:   http://localhost:8000/silk/
```

### Git Workflow

```bash
# Ver estado
git status

# Crear branch
git checkout -b feature/nueva-funcionalidad

# Commit
git add .
git commit -m "Descripción del cambio"

# Push
git push origin feature/nueva-funcionalidad

# Pull cambios remotos (prioritarios)
git fetch origin
git reset --hard origin/main  # CUIDADO: descarta cambios locales
```

### Base de Datos

```bash
# PostgreSQL (Node.js)
psql -U postgres -d axiomadb
\dt                    # Listar tablas
\d+ users             # Describir tabla

# MySQL (Django)
mysql -u root -p axiomaconnect
SHOW TABLES;
DESCRIBE productos_producto;

# Prisma Studio (GUI para PostgreSQL)
cd "C:\Ex drive\AXIOMA\ERP\project\Axioma-BE"
npx prisma studio
```

---

## 14. GLOSARIO DE TÉRMINOS

| Término | Definición |
|---------|-----------|
| **Tenant** | Organización o empresa que usa el sistema (multi-tenancy) |
| **Entity/Entidad** | Cliente o empresa comercial gestionada en el ERP |
| **JWT** | JSON Web Token - formato de autenticación |
| **RBAC** | Role-Based Access Control - control por roles |
| **ORM** | Object-Relational Mapping (Prisma, Django ORM) |
| **Soft Delete** | Marcar registros como eliminados sin borrarlos físicamente |
| **Audit Trail** | Registro de quién y cuándo modificó datos |
| **CORS** | Cross-Origin Resource Sharing - política de origen cruzado |
| **Middleware** | Función que intercepta peticiones HTTP |
| **Serializer** | Convierte objetos Python a JSON y viceversa (Django) |
| **ViewSet** | Clase que agrupa operaciones CRUD en Django REST |

---

## 15. CONTACTOS Y RECURSOS

### Repositorios
- **Frontend + Node.js**: `https://github.com/martin4yo/project.git`
- **Django Backend**: `https://github.com/martin4yo/AxiomaApi_2.0.git`

### Documentación Técnica Interna
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\README.md`
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\CLAUDE.md`
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\MEJORAS_IMPLEMENTADAS.md`

### Recursos Externos
- **React**: https://react.dev/
- **Django**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Prisma**: https://www.prisma.io/docs/
- **Express**: https://expressjs.com/
- **Vite**: https://vitejs.dev/

---

## 16. NOTAS FINALES

Este documento debe actualizarse cuando:
- Se agreguen nuevas funcionalidades importantes
- Cambien las configuraciones de base de datos o APIs
- Se implementen nuevas tecnologías o frameworks
- Cambien las URLs de producción o staging
- Se modifique la arquitectura del sistema

**Última actualización**: 2025-12-01

---

## 17. DISEÑO COMPLETO DE BASE DE DATOS (MVP)

**Fuente**: `Diseño MVP.drawio` - Diagrama completo con 7 páginas

El diseño del MVP incluye un esquema exhaustivo de la base de datos organizado en los siguientes módulos:

### 17.1. TABLAS GENERALES (Página 1 del Diagrama)

#### Documentación e Identificación
- **tipodocumento**: Id, Codigo (UK), Nombre, CodigoAfip (UK), IdMascara (FK), ScriptValidacion
- **mascara**: Id, Nombre, Estructura (define formatos de validación)
- **mascaratabla**: Id, Tabla, Campo, IdMascara (FK) - Asocia máscaras a campos

#### Geografía
- **pais**: Id, Codigo, Nombre, CodigoAfip
- **provincia**: Id, Codigo, Nombre, IdPais (FK), Jurisdiccion
- **partido**: Id, Codigo, Nombre, IdProvincia (FK), Jurisdiccion
- **codigopostal**: Id, Nombre, Codigo, IdPartido (FK)

#### Finanzas
- **moneda**: Id, Codigo, Nombre, AFIP
- **tipocambio**: Id, IdMoneda (FK), Importe, Vendedor, Comprador, Fecha
- **formapago**: Id, Codigo, Nombre, Habiles
- **formapagodetalle**: Id, IdFormaDePago (FK), Dias, Cuotas, Porcentaje

#### Comercio Internacional
- **incoterms**: Id, Codigo, Nombre
- **conceptoincluido**: Id, Codigo, Nombre

#### Sistema
- **modulo**: Id, Nombre, Codigo (UK)
- **sector**: Id, Nombre, Codigo (UK)
- **idiomas**: Id, Codigo, Nombre
- **parametro**: Id, IdModulo (FK), NombreParametro, IdTipoDato (FK), Valor
- **tipodato**: Id, Codigo, Nombre

#### Medidas y Unidades
- **unidadmedida**: Id, Codigo, Nombre, CodigoAfip, SI, NumeroDecimales

#### Impuestos y Fiscalidad
- **tiporesponsable**: Id, Codigo, Nombre, Sigla
- **tiposujeto**: Id, Codigo, Nombre
- **tipoimpuesto**: Id, Codigo, Nombre, IdClasificacion (FK)
- **clasificacionimpuesto**: Id, Codigo, Nombre (indica si es "Otros Tributos" AFIP)
- **impuesto**: Id, Codigo, Nombre, IdTipoImpuestos (FK), IdAlicuota (FK), IdPlanCuenta (FK), CalculaPadron, IdPadron (FK), IdProvincia (FK), IdPartido (FK)
- **alicuotaimpuesto**: Id, Codigo, Nombre, Porcentaje, CodigoFiscal
- **padronimpuesto**: Id, Codigo, Nombre, IdTipoCalculo (FK)
- **tipocalculo**: Id, Codigo, Nombre
- **cuitpais**: Id, IdPais (FK), IdTipoSujetoFiscal (FK), IdTipoDocumento (FK = '80'), Cuit

#### Comprobantes Fiscales
- **tipocomprobantefiscal**: Id, Codigo, Nombre, EsCredito, Letra
- **formulariofiscal**: Id, IdTipoComprobanteFiscal (FK), Codigo, Nombre, IdPuntoVenta (FK), UltimoNumero
- **comprobanteresponsable**: Id, IdModulo (FK), IdTipoResponsable (FK), IdTipoComprobanteFiscal (FK)
- **puntoventa**: Id, Codigo, Nombre, PuntoVenta, IdSucursal (FK)
- **sucursal**: Id, Codigo, Nombre

#### Índices y Ajustes
- **indices**: Id, IdTipoIndice (FK), Desde, Hasta, Importe
- **tipoindice**: Id, Codigo, Nombre, IdMoneda (FK), IdTipoFrecuencia (FK), IdTipovalor (FK)
- **tipofrecuencia**: Id, Codigo, Nombre
- **tipovalor**: Id, Codigo, Nombre

---

### 17.2. PERMISOS Y SEGURIDAD (Página 2 del Diagrama)

#### Usuarios y Roles
- **persona**: Id, Nombre, Direccion, IdCodigoPostal (FK), Telefono, Usuario, Password, Mail
- **rol**: Id, Nombre
- **personarol**: Id, IdPersona (FK), IdRol (FK)

#### Permisos Dinámicos
- **permisosrol**: Id, IdRol (FK), IdModulo (FK), [A definir...]
- **permisoformulario**: Id, IdFormulario (UK), Nombre, Tenant
- **permisocampo**: Id, IdCampo, IdFormulario, Nombre, Visible, Editable

**Nota**: Este módulo permite configurar permisos a nivel de formulario y campo individualmente, dando máxima flexibilidad.

---

### 17.3. ENTIDADES COMERCIALES (Página 3 del Diagrama)

#### Entidad Principal
- **entidad**: Id, Codigo (UK), NombreFantasia, RazonSocial, IdTipoResponsable (FK), Intercompany (Check)

#### Relaciones de Entidad
- **ejecutivo**: Id, IdEntidad (FK), IdPersona (FK), IdRol (FK)
  - Personas asignadas a la entidad con roles específicos

- **datosfiscalesentidad**: Id, IdEntidad (FK), IdTipoDocumento (FK), NumeroDocumento, IdTipoSujetoFiscal (FK)
  - Información fiscal de la entidad

- **contactoentidad**: Id, IdEntidad (FK), NombreContacto, RolContactoEntidad, TelefonoContactoEntidad, MailContactoEntidad
  - Contactos asociados a la entidad

- **direccionentidad**: Id, IdEntidad (FK), Nombre, IdSedeEntidad (FK), IdTipoDomicilio (FK), Calle, Numero, Piso, Departamento, Pais (FK), Provincia (FK), Partido (FK), IdCodigoPostal (FK), IdZona (FK), DiasEntrega, DiasRetiro
  - Múltiples direcciones por entidad

#### Configuraciones por Módulo
- **listaprecioentidad**: Id, IdEntidad (FK), IdModulo (FK), IdListaPrecio (FK)
  - UK: IdEntidad + IdModulo + IdListaPrecio

- **impuestoentidad**: Id, IdEntidad (FK), IdModulo (FK), IdImpuesto (FK), AplicaExencion, PorcentajeExencion, Resolucion, VigenciaDesde, VigenciaHasta
  - Impuestos aplicables a la entidad

- **condicioncrediticia**: Id, IdEntidad (FK), IdModulo (FK), VigenciaDesde, VigenciaHasta, LimiteDesde, LimiteHasta
  - Condiciones de crédito por módulo

- **formapagoentidad**: Id, IdEntidad (FK), IdModulo (FK), IdFormaPago (FK)
  - Formas de pago habilitadas

- **sectorentidad**: Id, IdEntidad (FK), IdModulo (FK), IdSector (FK)
  - Sector comercial

- **moduloentidad**: Id, IdEntidad (FK), IdModulo (FK)
  - Módulos habilitados para la entidad

#### Tablas de Soporte
- **zona**: Id, Codigo (UK), Nombre
- **sede**: Id, Codigo (UK), Nombre (ej: Casa Central, Sucursal Norte)
- **tipodomicilio**: Id, Codigo (UK), Nombre (ej: Fiscal, Entrega, Facturación)

---

### 17.4. PRODUCTOS (Página 4+ del Diagrama)

#### Producto Principal
- **producto**: Id, IdTipoProducto (FK), Codigo (UK), Nombre, ModificaTexto, Ean (UK), IdUnidadMedida (FK), IdClaseProducto (FK), Decimales, StockMinimo, StockMaximo, PuntoPedido, AvisoPedido, AvisoMinimo, [continúa...]

#### Clasificación de Productos
- **tipoproducto**: Id, Codigo (UK), Nombre, Stockeable, BienUso
  - Define si el producto es almacenable o bien de uso

- **claseproducto**: Id, Codigo, Nombre
  - Clasificación adicional de productos

#### Precios
- **precio**: [Estructura pendiente de exploración completa]
- **listaprecio**: [Estructura pendiente de exploración completa]

#### Atributos Dinámicos
- **atributo**, **atributotipo**, **atributoproducto**, **atributovalor**
  - Sistema de atributos configurables para productos

---

### 17.5. RELACIONES CLAVE Y CLAVES ÚNICAS

#### Unique Keys Identificadas
- **entidad**: Codigo
- **producto**: Codigo, Ean
- **listaprecioentidad**: (IdEntidad, IdModulo, IdListaPrecio)
- **permisoformulario**: IdFormulario
- **tipodocumento**: Codigo, CodigoAfip
- **modulo**: Codigo
- **sector**: Codigo

#### Foreign Keys Principales
Todas las tablas relacionadas implementan FKs apropiadas con convención:
- `Id{NombreTabla}` para referencias (ej: IdEntidad, IdProducto, IdModulo)
- Múltiples FKs por tabla cuando se relacionan con varias entidades

---

### 17.6. CONVENCIONES DEL DISEÑO

1. **Primary Keys**: Todas las tablas usan `Id (PK)` como identificador autoincremental
2. **Códigos Únicos**: Tablas maestras tienen `Codigo (UK)` para identificación de negocio
3. **Multi-Módulo**: Muchas tablas incluyen `IdModulo (FK)` para segregar datos por módulo
4. **Auditoría**: (Implementado en Django/Prisma, no visible en diagrama)
5. **Soft Delete**: (Implementado en capa de aplicación)
6. **Tenant**: Multi-tenant manejado en capa de aplicación

---

### 17.7. COLORES EN EL DIAGRAMA (Significado)

- **Morado (#e1d5e7)**: Tablas estándar del sistema
- **Verde (#00FF00)**: Tablas pendientes de implementación o en desarrollo
- **Rosa/Rojo (#f8cecc)**: Tablas de permisos dinámicos
- **Verde oscuro (#26f31b)**: Tablas fiscales/comprobantes

---

## 18. APÉNDICE: ESQUEMAS DE BASE DE DATOS

### PostgreSQL (Node.js) - Tablas Principales

```sql
-- Users
users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  username VARCHAR(100),
  password VARCHAR(255) NOT NULL,
  client_id INT REFERENCES clients(id),
  refresh_token TEXT,
  reset_password_token TEXT,
  registered_by_google BOOLEAN DEFAULT FALSE,
  is_profile_completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
)

-- Tenants
tenants (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  url_identifier VARCHAR(100) UNIQUE NOT NULL,
  logo_url VARCHAR(500),
  logo_url_dark VARCHAR(500),
  is_active BOOLEAN DEFAULT TRUE
)

-- Roles
roles (
  id SERIAL PRIMARY KEY,
  role VARCHAR(50) UNIQUE NOT NULL,
  is_active BOOLEAN DEFAULT TRUE
)

-- Clients
clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  celocity_percentage DECIMAL(5,2),
  tenant_id INT REFERENCES tenants(id),
  is_active BOOLEAN DEFAULT TRUE
)

-- Contacts
contacts (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(50),
  name VARCHAR(100),
  last_name VARCHAR(100),
  tenant_id INT REFERENCES tenants(id)
)
```

### MySQL (Django) - Tablas Principales

```sql
-- Productos
productos_producto (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  tenant_id BIGINT NOT NULL,
  codigo VARCHAR(50) NOT NULL,
  nombre VARCHAR(200) NOT NULL,
  descripcion TEXT,
  is_active BOOLEAN DEFAULT TRUE,
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW(),
  disabled BOOLEAN DEFAULT FALSE,
  user_id BIGINT,
  UNIQUE KEY unique_tenant_codigo (tenant_id, codigo)
)

-- Entidades
entidades_entidad (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  tenant_id BIGINT NOT NULL,
  codigo VARCHAR(50) NOT NULL,
  nombre VARCHAR(200) NOT NULL,
  razon_social VARCHAR(200),
  cuit VARCHAR(13),
  tipo_entidad_id BIGINT,
  is_active BOOLEAN DEFAULT TRUE,
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW(),
  disabled BOOLEAN DEFAULT FALSE,
  user_id BIGINT,
  UNIQUE KEY unique_tenant_codigo (tenant_id, codigo)
)

-- Impuestos
impuestos_impuesto (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  tenant_id BIGINT NOT NULL,
  codigo VARCHAR(50) NOT NULL,
  nombre VARCHAR(200) NOT NULL,
  tipo_impuesto_id BIGINT,
  alicuota DECIMAL(5,2),
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW(),
  disabled BOOLEAN DEFAULT FALSE,
  user_id BIGINT
)

-- Personas (usuarios en Django)
general_persona (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  tenant_id BIGINT NOT NULL,
  username VARCHAR(150) UNIQUE NOT NULL,
  email VARCHAR(254) UNIQUE NOT NULL,
  password VARCHAR(128) NOT NULL,
  first_name VARCHAR(150),
  last_name VARCHAR(150),
  is_active BOOLEAN DEFAULT TRUE,
  created_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW()
)
```

---

## 19. DESCRIPCIÓN DETALLADA DE CAMPOS Y LÓGICA DE NEGOCIO

**Fuente**: `Descripcion de campos de tablas.docx` - Documento con definiciones completas de negocio

Este documento contiene la descripción detallada de cada campo de las tablas del sistema, incluyendo la lógica de negocio, validaciones y reglas. A continuación se resumen las secciones principales:

### 19.1. CONVENCIONES GENERALES

- **PK** = Primary Key
- **FK** = Foreign Key (referencia a otra tabla con patrón Id{NombreTabla})
- **UK** = Unique Key (con máscara de validación)
- **C** = Check constraint
- **IdModulo (FK)** = Todas las tablas de configuración por módulo referencian a la tabla modulo
- **Soft Delete** = Registros marcados como deshabilitados (disabled) en lugar de eliminación física
- **Audit Trail** = created_at, updated_at, user_id en todas las tablas

### 19.2. TABLAS GENERALES

#### modulo
- **Id (PK)**: Identificador único
- **Nombre**: Descripción del módulo (Ventas, Compras, Producción, Contabilidad, etc.)
- **Codigo (UK)**: Código único alfanumérico del módulo

#### mascaras
Define los formatos de validación para códigos y campos del sistema.
- **Id (PK)**: Identificador único
- **Nombre**: Nombre descriptivo de la máscara
- **Estructura**: Define el tipo de carácter (letra/número) y la cantidad de posiciones
  - Ejemplo: "LLNNNN" = 2 letras seguidas de 4 números
  - Validación automática en inserción/actualización de registros

#### persona
Usuarios del sistema con autenticación y roles.
- **Id (PK)**: Identificador único
- **Nombre**: Nombre completo del usuario
- **Usuario**: Username para login
- **Password**: Contraseña hasheada
- **Mail**: Email del usuario (usado para recuperación de contraseña)

#### tipodocumento
Tipos de documentos de identidad con integración AFIP.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código interno del tipo de documento (con máscara)
- **Nombre**: Descripción (DNI, CUIT, CUIL, Pasaporte, etc.)
- **CodigoAfip (UK)**: Código oficial de AFIP para facturación electrónica
- **IdMascara (FK)**: Referencia a la máscara de validación
- **ScriptValidacion**: Script adicional para validaciones complejas (ej: dígito verificador de CUIT)

#### tiporesponsable
Categorías fiscales según AFIP.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código del tipo de responsable
- **Nombre**: Descripción completa
- **Sigla**: Sigla representativa
  - Ejemplo: "RI" = Responsable Inscripto, "MT" = Monotributo, "EX" = Exento, "CF" = Consumidor Final

#### pais, provincia, partido, codigopostal
Jerarquía geográfica para direcciones.
- Cada nivel referencia al nivel superior mediante FK
- **Jurisdiccion**: Campo en provincia/partido que indica jurisdicción fiscal
- **CodigoAfip**: Integración con sistema de AFIP en provincia

#### moneda, tipocambio
Sistema de monedas y tipos de cambio.
- **moneda**: Monedas del sistema (ARS, USD, EUR, etc.) con código AFIP
- **tipocambio**: Histórico de cotizaciones con fecha
  - **Vendedor**: Tipo de cambio vendedor
  - **Comprador**: Tipo de cambio comprador
  - **Importe**: Cotización oficial

#### formapago, formapagodetalle
Formas de pago con cuotas y plazos.
- **formapago**: Forma de pago principal (Contado, Cheque, Transferencia, etc.)
  - **Habiles**: Indica si los días son hábiles o corridos
- **formapagodetalle**: Detalle de cuotas y plazos
  - **Dias**: Días de plazo para cada cuota
  - **Cuotas**: Cantidad de cuotas
  - **Porcentaje**: Porcentaje del total para esta cuota

#### impuesto, alicuotaimpuesto, padronimpuesto
Sistema completo de impuestos.
- **tipoimpuesto**: Clasificación de impuestos
  - **IdClasificacion (FK)**: Referencia a clasificacionimpuesto
  - Determina si es "Otros Tributos" para AFIP

- **impuesto**: Impuesto específico
  - **Codigo (UK)**: Código único del impuesto
  - **Nombre**: IVA, Percepción IVA, Ingresos Brutos, etc.
  - **IdTipoImpuestos (FK)**: Tipo de impuesto
  - **IdAlicuota (FK)**: Alícuota predeterminada
  - **IdPlanCuenta (FK)**: Cuenta contable asociada
  - **CalculaPadron**: Si se debe calcular según padrón
  - **IdPadron (FK)**: Referencia al padrón si aplica
  - **IdProvincia (FK), IdPartido (FK)**: Jurisdicción territorial

- **alicuotaimpuesto**: Alícuotas de impuestos
  - **Codigo (UK)**: Código de la alícuota
  - **Porcentaje**: Porcentaje del impuesto
  - **CodigoFiscal**: Código para facturación electrónica

- **padronimpuesto**: Padrón de contribuyentes
  - **IdTipoCalculo (FK)**: Cómo se calcula (porcentaje, importe fijo, etc.)

#### tipocomprobantefiscal, formulariofiscal
Comprobantes fiscales según AFIP.
- **tipocomprobantefiscal**: Tipos de comprobantes (Factura A, B, C, Nota de Crédito, etc.)
  - **EsCredito**: Indica si es documento de crédito o débito
  - **Letra**: Letra del comprobante (A, B, C, E, etc.)

- **formulariofiscal**: Numeración de comprobantes
  - **IdTipoComprobanteFiscal (FK)**: Tipo de comprobante
  - **IdPuntoVenta (FK)**: Punto de venta asociado
  - **UltimoNumero**: Último número utilizado (para generar siguiente)

#### puntoventa, sucursal
Puntos de venta físicos o virtuales.
- **sucursal**: Sucursales de la empresa
- **puntoventa**: Puntos de venta por sucursal
  - **PuntoVenta**: Número de punto de venta AFIP
  - **IdSucursal (FK)**: Sucursal asociada

### 19.3. ENTIDADES COMERCIALES

#### entidad
Entidad comercial principal (clientes, proveedores, etc.)
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código único de la entidad (con máscara)
- **NombreFantasia**: Nombre comercial
- **RazonSocial**: Razón social fiscal
- **IdTipoResponsable (FK)**: Categoría fiscal (RI, MT, etc.)
- **Intercompany (C)**: Check para marcar si es entidad intercompany

#### ejecutivo
Personas asociadas a una entidad con roles específicos.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdPersona (FK)**: Persona que actúa como ejecutivo
- **IdRol (FK)**: Rol del ejecutivo (vendedor, comprador, gerente, etc.)

#### datosfiscalesentidad
Información fiscal de la entidad.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdTipoDocumento (FK)**: Tipo de documento fiscal
- **NumeroDocumento**: Número del documento (CUIT/CUIL)
- **IdTipoSujetoFiscal (FK)**: Tipo de sujeto fiscal

#### contactoentidad
Personas de contacto de la entidad.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **NombreContacto**: Nombre del contacto
- **RolContactoEntidad**: Rol/puesto del contacto
- **TelefonoContactoEntidad**: Teléfono de contacto
- **MailContactoEntidad**: Email de contacto

#### direccionentidad
Direcciones múltiples por entidad.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **Nombre**: Nombre descriptivo de la dirección
- **IdSedeEntidad (FK)**: Sede de la entidad
- **IdTipoDomicilio (FK)**: Tipo (fiscal, entrega, facturación, etc.)
- **Calle, Numero, Piso, Departamento**: Dirección completa
- **IdCodigoPostal (FK)**: Código postal
- **IdZona (FK)**: Zona de reparto
- **DiasEntrega**: Días de entrega para esta dirección
- **DiasRetiro**: Días de retiro desde esta dirección

#### listaprecioentidad
Lista de precios aplicable a la entidad por módulo.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdModulo (FK)**: Módulo (ventas, compras, etc.)
- **IdListaPrecio (FK)**: Lista de precios aplicable
- **UK**: (IdEntidad, IdModulo, IdListaPrecio)

#### condicioncrediticia
Condiciones de crédito por entidad y módulo.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdModulo (FK)**: Módulo aplicable
- **VigenciaDesde, VigenciaHasta**: Período de vigencia
- **LimiteDesde, LimiteHasta**: Límites de crédito

#### impuestoasociadoentidad (impuestoentidad en diagrama)
Impuestos específicos aplicables a la entidad.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdModulo (FK)**: Módulo aplicable
- **IdImpuesto (FK)**: Impuesto asociado
- **AplicaExencion**: Si aplica exención del impuesto
- **PorcentajeExencion**: Porcentaje de exención
- **Resolucion**: Número de resolución de exención
- **VigenciaDesde, VigenciaHasta**: Período de vigencia de la exención

#### formapagoentidad
Formas de pago habilitadas para la entidad.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdModulo (FK)**: Módulo aplicable
- **IdFormaPago (FK)**: Forma de pago habilitada

#### sectorentidad
Sector comercial de la entidad por módulo.
- **Id (PK)**: Identificador único
- **IdEntidad (FK)**: Entidad asociada
- **IdModulo (FK)**: Módulo aplicable
- **IdSector (FK)**: Sector comercial (retail, mayorista, industria, etc.)

### 19.4. PRODUCTOS

#### producto
Producto principal del catálogo.
- **Id (PK)**: Identificador único
- **IdTipoProducto (FK)**: Tipo de producto (mercadería, servicio, bien de uso)
- **Codigo (UK)**: Código único del producto (con máscara)
- **Nombre**: Nombre descriptivo del producto
- **ModificaTexto**: Permite modificar descripción en comprobantes
- **Ean (UK)**: Código de barras EAN único
- **IdUnidadMedida (FK)**: Unidad de medida (kg, litros, unidades, etc.)
- **IdClaseProducto (FK)**: Clasificación del producto
- **Decimales**: Cantidad de decimales para cantidades
- **StockMinimo**: Stock mínimo de seguridad
- **StockMaximo**: Stock máximo permitido
- **PuntoPedido**: Punto en el que se debe realizar pedido
- **AvisoPedido**: Genera aviso al llegar al punto de pedido
- **AvisoMinimo**: Genera aviso al llegar al mínimo

#### tipoproducto
Tipos de productos.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código del tipo
- **Nombre**: Descripción (Mercadería, Servicio, Bien de Uso, etc.)
- **Stockeable**: Si el producto lleva control de stock
- **BienUso**: Si es un bien de uso (activo fijo)

#### claseproducto
Clasificación adicional de productos.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código de la clase
- **Nombre**: Descripción de la clasificación

#### conversionproducto
Conversiones entre unidades de medida del producto.
- **Id (PK)**: Identificador único
- **IdProducto (FK)**: Producto asociado
- **IdUnidadMedidaOrigen (FK)**: Unidad de medida origen
- **IdUnidadMedidaDestino (FK)**: Unidad de medida destino
- **Factor**: Factor de conversión

#### contabilidadproducto
Configuración contable del producto.
- **Id (PK)**: Identificador único
- **IdProducto (FK)**: Producto asociado
- **IdPlanCuenta (FK)**: Cuenta contable asociada
- Diferentes cuentas según operación (ventas, compras, inventario, etc.)

#### atributo, atributovalor, atributoproducto
Sistema de atributos dinámicos.
- **atributo**: Definición del atributo (Color, Talle, Marca, etc.)
  - **IdTipoAtributo (FK)**: Tipo de dato (texto, número, fecha, lista)

- **atributovalor**: Valores posibles para atributos de tipo lista
  - **IdAtributo (FK)**: Atributo asociado
  - **Valor**: Valor del atributo

- **atributoproducto**: Valores de atributos asignados a productos
  - **IdProducto (FK)**: Producto asociado
  - **IdAtributo (FK)**: Atributo asociado
  - **Valor**: Valor del atributo para este producto

#### listavalor, valorproducto
Listas de valores adicionales para productos.
- **listavalor**: Definición de listas de valores personalizadas
- **valorproducto**: Valores asignados a productos

### 19.5. COMPROBANTES

#### comprobantecabecera
Cabecera de comprobantes del sistema.
- **Id (PK)**: Identificador único
- **IdModulo (FK)**: Módulo que genera el comprobante
- **IdTipoComprobanteFiscal (FK)**: Tipo de comprobante
- **IdFormularioFiscal (FK)**: Formulario fiscal utilizado
- **IdEntidad (FK)**: Entidad asociada (cliente/proveedor)
- **Fecha**: Fecha del comprobante
- **Numero**: Número del comprobante
- Campos adicionales para totales, impuestos, etc.

#### comprobantetiporegistracion, tiporegistracion
Tipos de registración contable para comprobantes.
- **tiporegistracion**: Define tipos de asientos contables generados
- **comprobantetiporegistracion**: Asocia comprobantes con tipos de registración

### 19.6. CONTABILIDAD

#### clasificacioncontable
Clasificación del plan de cuentas contable.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código de clasificación
- **Nombre**: Descripción (Activo, Pasivo, Patrimonio Neto, Resultado Positivo, Resultado Negativo)

#### funcionamientocontable
Define el funcionamiento de las cuentas contables.
- **Id (PK)**: Identificador único
- **Codigo (UK)**: Código del funcionamiento
- **Nombre**: Descripción (Deudora, Acreedora)
- Determina si la cuenta aumenta por el debe o por el haber

### 19.7. VALIDACIONES Y REGLAS DE NEGOCIO

#### Máscaras de Validación
Las máscaras definen el formato exacto que debe cumplir un código:
- **L** = Letra mayúscula
- **N** = Número
- **X** = Letra o número
- Ejemplo: "LLNNNN" valida códigos como "AB1234"

#### Scripts de Validación
Algunos campos tienen scripts de validación complejos:
- **CUIT**: Validación de dígito verificador
- **Códigos AFIP**: Validación contra tablas oficiales
- **Fechas de vigencia**: Validación de rangos sin solapamiento

#### Constraints y Checks
- **Unique Keys**: Garantizan unicidad de códigos por tenant
- **Check Constraints**: Validan rangos de valores (ej: porcentajes 0-100)
- **Foreign Keys**: Integridad referencial entre tablas
- **Not Null**: Campos obligatorios según reglas de negocio

#### Reglas Multi-Tenant
- Todos los códigos únicos son únicos **por tenant** (tenant_id + codigo)
- Las búsquedas siempre filtran por tenant_id
- No se puede acceder a datos de otros tenants

#### Soft Delete Pattern
- Los registros nunca se eliminan físicamente
- Campo `disabled = true` marca registros como eliminados
- Las consultas filtran automáticamente registros deshabilitados
- Se mantiene integridad histórica de comprobantes

### 19.8. INTEGRACIÓN CON AFIP

El sistema está preparado para integración completa con AFIP:
- **Códigos AFIP**: Todos los maestros tienen códigos oficiales
- **Comprobantes Electrónicos**: Sistema de numeración automática
- **Tipos de Responsable**: Categorías fiscales oficiales
- **Impuestos**: Alícuotas y códigos fiscales según normativa
- **Documentos**: Validación según tablas AFIP
- **Padrón**: Sistema de consulta de padrón de contribuyentes

---

## 20. DOCUMENTACIÓN ADICIONAL DISPONIBLE

Los siguientes documentos contienen información adicional sobre el sistema:

### Documentos Analizados
1. **Diseño MVP.drawio** - Diagrama completo de base de datos (7 páginas)
2. **Descripcion de campos de tablas.docx** - Lógica de negocio y definiciones (640 líneas)

### Documentos Pendientes de Análisis
3. **Doc de diseño para AI.docx** - Documento de diseño específico para desarrollo con IA
4. **Logica de Negocio.docx** - Reglas de negocio adicionales
5. **Opciones Axioma.docx** - Configuraciones y opciones del sistema

### Documentación Técnica Interna
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\README.md`
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\CLAUDE.md`
- `C:\Ex drive\AXIOMA\ERP\AxiomaApi_2.0\MEJORAS_IMPLEMENTADAS.md`

---

**FIN DEL DOCUMENTO DE REFERENCIA**

**Última actualización**: 2025-12-01
**Secciones**: 20
**Páginas del diseño analizadas**: 7
**Documentos Word analizados**: 1 de 4
