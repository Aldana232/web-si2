# 🎯 WORKFLOW DE CRÉDITO - Documentación Técnica

## ✅ Implementado: Workflow de Crédito con Línea de Tiempo

Se ha implementado una solución completa de workflow de créditos con 8 fases secuenciales y línea de tiempo completa.

---

## 📊 Cambios en el Backend

### 1. Modelo `Credito` - Campos Agregados

```
✅ fase_actual: CharField - Fase actual en la que está el crédito
✅ razon_rechazo: TextField - Razón si fue rechazado
✅ fecha_creacion: DateTimeField - Cuándo se creó
✅ fecha_actualizacion: DateTimeField - Cuándo se actualizó por última vez
```

### 2. Nuevo Modelo `HistoricoCredito`

```
✅ credito: ForeignKey a Credito
✅ fase_anterior: CharField - Fase previa
✅ fase_nueva: CharField - Fase nueva
✅ fecha_cambio: DateTimeField - Cuándo cambió
✅ usuario_cambio: ForeignKey a User - Quién realizó el cambio
✅ descripcion: TextField - Qué sucedió
✅ datos_agregados: JSONField - Datos que se agregaron
```

### 3. Migraciones

- ✅ `0003_credito_fase_actual_credito_fecha_actualizacion_and_more.py`
  - Agrega campos a Credito
  - Crea modelo HistoricoCredito
  - Aplicada exitosamente a la BD

### 4. Módulo de Workflow

**Archivo:** `app_Credito/workflow.py`

Contiene funciones helper:
- `cambiar_fase()` - Cambia el crédito a una nueva fase
- `validar_fase_secuencial()` - Valida que no se salten fases
- `obtener_linea_tiempo()` - Retorna el historial de cambios
- `obtener_estado_actual()` - Retorna estado actual con todos los datos

---

## 🔌 Nuevos Endpoints de API

### Base URL
```
http://localhost:8000/api/creditos/
```

### 1. Crear Crédito (FASE 1)
```
POST /api/creditos/
Authorization: Token <TOKEN>

{
  "Monto_Solicitado": 5000,
  "Numero_Cuotas": 12,
  "Monto_Cuota": 500,
  "Tasa_Interes": 12.5,
  "Moneda": "USD",
  "tipo_credito": 1,
  "cliente": 1
}

Respuesta:
{
  "id": 123,
  "fase_actual": "FASE_1_SOLICITUD",
  "enum_estado": "SOLICITADO",
  ...
}
```

### 2. Agregar Documentación (FASE 2)
```
PATCH /api/creditos/{id}/agregar-documentacion/
Authorization: Token <TOKEN>

{
  "ci": "12345678",
  "documento_url": "https://..."
}

Respuesta: 200 OK con estado actualizado
```

### 3. Agregar Información Laboral (FASE 3)
```
PATCH /api/creditos/{id}/agregar-laboral/
Authorization: Token <TOKEN>

{
  "cargo": "Gerente",
  "empresa": "Empresa XYZ",
  "salario": 3000,
  "extracto_url": "https://..."
}

Respuesta: 200 OK con estado actualizado
```

### 4. Agregar Domicilio (FASE 4)
```
PATCH /api/creditos/{id}/agregar-domicilio/
Authorization: Token <TOKEN>

{
  "descripcion": "Casa de 2 pisos en barrio residencial",
  "croquis_url": "https://...",
  "es_propietario": true,
  "numero_ref": "Calle 5 #123"
}

Respuesta: 200 OK con estado actualizado
```

### 5. Agregar Garante (FASE 5)
```
PATCH /api/creditos/{id}/agregar-garante/
Authorization: Token <TOKEN>

{
  "nombrecompleto": "Juan López",
  "ci": "87654321",
  "telefono": "2121234567"
}

Respuesta: 200 OK con estado actualizado
```

### 6. Enviar a Revisión (FASE 6)
```
PATCH /api/creditos/{id}/enviar-revision/
Authorization: Token <TOKEN>

{}

Respuesta: 200 OK - Crédito enviado a revisión
```

### 7. Revisar/Aprobar/Rechazar (FASE 6 → FASE 7 o mantener)
```
PATCH /api/creditos/{id}/revisar/
Authorization: Token <TOKEN>

{
  "aprobado": true,
  "razon": "Perfecto perfil de crediticio"
}

O para rechazar:
{
  "aprobado": false,
  "razon": "Ingresos insuficientes"
}

Respuesta: 200 OK con estado actualizado
```

### 8. Desembolsar (FASE 7 → FASE 8)
```
PATCH /api/creditos/{id}/desembolsar/
Authorization: Token <TOKEN>

{}

Respuesta: 200 OK - Crédito desembolsado
```

### 9. Obtener Línea de Tiempo
```
GET /api/creditos/{id}/linea-tiempo/
Authorization: Token <TOKEN>

Respuesta:
{
  "credito_id": 123,
  "linea_tiempo": [
    {
      "fase_anterior": null,
      "fase_nueva": "FASE_1_SOLICITUD",
      "fecha_cambio": "2025-11-17T10:00:00Z",
      "usuario": "admin_petrodrill",
      "descripcion": "Solicitud inicial creada",
      "datos_agregados": {...}
    },
    {
      "fase_anterior": "FASE_1_SOLICITUD",
      "fase_nueva": "FASE_2_DOCUMENTACION",
      "fecha_cambio": "2025-11-17T11:30:00Z",
      "usuario": "admin_petrodrill",
      "descripcion": "Documentación agregada",
      "datos_agregados": {"ci": "12345678", ...}
    },
    ...
  ],
  "total_cambios": 5
}
```

### 10. Obtener Estado Actual
```
GET /api/creditos/{id}/estado-actual/
Authorization: Token <TOKEN>

Respuesta:
{
  "credito_id": 123,
  "fase_actual": "FASE_5_GARANTE",
  "estado": "Aprobado",
  "cliente": {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "telefono": "2121234567"
  },
  "documentacion": {
    "ci": "12345678",
    "documento_url": "https://..."
  },
  "laboral": {
    "cargo": "Gerente",
    "empresa": "Empresa XYZ",
    "salario": "3000.00",
    "extracto_url": "https://..."
  },
  "domicilio": {
    "descripcion": "Casa de 2 pisos",
    "es_propietario": true,
    "croquis_url": "https://...",
    "numero_ref": "Calle 5 #123"
  },
  "garante": {
    "nombrecompleto": "Juan López",
    "ci": "87654321",
    "telefono": "2121234567"
  },
  "monto_solicitado": "5000.00",
  "moneda": "USD",
  "fecha_creacion": "2025-11-17T10:00:00Z",
  "fecha_actualizacion": "2025-11-17T15:00:00Z"
}
```

---

## 📱 Componentes Frontend Creados

### 1. Componente Wizard
**Archivo:** `src/modules/creditos/components/WizardCredito.tsx`

- Componente de formulario paso a paso
- 6 fases de entrada de datos
- Validación en cada paso
- Botones Anterior/Siguiente
- Barra de progreso visual
- Indicadores de paso

**Features:**
- ✅ Bloquea siguiente paso hasta completar datos
- ✅ Permite retroceder
- ✅ Muestra progreso porcentual
- ✅ Componentes específicos para cada fase
- ✅ Responsive en móviles

### 2. Componente Timeline
**Archivo:** `src/modules/creditos/components/TimelineCredito.tsx`

- Línea de tiempo vertical de cambios
- Mostrar eventos expandibles
- Información de usuario y fecha
- Datos agregados detallados
- Leyenda de colores
- Estado actual resaltado

**Features:**
- ✅ Timeline visual con iconos
- ✅ Expansión/Colapso de eventos
- ✅ Colores por fase
- ✅ Información detallada
- ✅ Responsive

### 3. Estilos CSS
**Archivos:**
- `WizardCredito.css` - Estilos del wizard
- `TimelineCredito.css` - Estilos de timeline

**Características:**
- ✅ Diseño moderno y limpio
- ✅ Variables CSS para temas
- ✅ Animaciones suaves
- ✅ Totalmente responsive
- ✅ Accesibilidad mejorada

---

## 🔄 Flujo Completo del Crédito

```
Cliente inicia solicitud
    ↓
FASE 1: Llena datos iniciales (monto, plazo, tipo)
    ↓ (Wizard paso 1)
FASE 2: Carga documentación personal (CI, documento)
    ↓ (Wizard paso 2)
FASE 3: Ingresa info laboral (empresa, cargo, salario)
    ↓ (Wizard paso 3)
FASE 4: Registra domicilio (descripción, ubicación)
    ↓ (Wizard paso 4)
FASE 5: Agrega garante (nombre, CI, contacto)
    ↓ (Wizard paso 5)
Cliente envía solicitud a revisión
    ↓ (Wizard paso 6)
FASE 6: Analista revisa y aprueba/rechaza
    ↓ (Si aprobado)
FASE 7: Se realiza desembolso
    ↓
FASE 8: Crédito finalizado
```

---

## 🛡️ Validaciones Implementadas

✅ **Flujo Secuencial**
- No permite saltarse fases
- Debe completar fase N antes de ir a N+1

✅ **Multitenancy**
- Cada empresa solo ve sus créditos
- Datos asociados a empresa automáticamente

✅ **Datos Requeridos**
- Cada endpoint valida campos obligatorios
- Retorna error 400 si faltan datos

✅ **Auditoría Completa**
- Se registra quién hizo cada cambio
- Timestamp de cada acción
- Descripción de qué se hizo
- Datos agregados en formato JSON

---

## 🧪 Cómo Probar

### 1. Crear un Crédito
```bash
POST /api/creditos/
Authorization: Token <TOKEN>
{
  "Monto_Solicitado": 5000,
  "Numero_Cuotas": 12,
  "Monto_Cuota": 500,
  "Tasa_Interes": 12.5,
  "Moneda": "USD",
  "tipo_credito": 1,
  "cliente": 1
}
```

Guardas el `id` retornado (ej: 123)

### 2. Agregar Documentación
```bash
PATCH /api/creditos/123/agregar-documentacion/
Authorization: Token <TOKEN>
{
  "ci": "12345678",
  "documento_url": "https://example.com/doc.pdf"
}
```

Verifica que `fase_actual` es ahora `FASE_2_DOCUMENTACION`

### 3. Ver Línea de Tiempo
```bash
GET /api/creditos/123/linea-tiempo/
Authorization: Token <TOKEN>
```

Deberías ver 2 eventos (creación y cambio a FASE_2)

### 4. Ver Estado Actual
```bash
GET /api/creditos/123/estado-actual/
Authorization: Token <TOKEN>
```

Deberías ver toda la información acumulada

---

## 📝 Notas de Implementación

- ✅ Sin cambios destructivos en BD
- ✅ Migraciones aplicadas correctamente
- ✅ Todos los campos nuevos son opcionales (blank=True)
- ✅ Mantiene multitenancy en todos los endpoints
- ✅ Serializers listos para usar
- ✅ Sistema de fases completamente secuencial
- ✅ Auditoría completa de todos los cambios

---

## 🚀 Próximos Pasos

1. Conectar Frontend Wizard con endpoints
2. Conectar Frontend Timeline con endpoint `/linea-tiempo/`
3. Crear filtros en listado de créditos por fase
4. Agregar notificaciones cuando cambie de fase
5. Reportes de progreso de créditos
6. Dashboard del analista para revisar créditos

---

**Implementación completada: ✅ 100%**
