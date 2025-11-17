# 🎯 Guía de Prueba - Sistema de Workflow de Créditos

## ✅ Estado del Sistema

**Backend:** ✅ OK (0 errores)  
**Frontend:** ✅ OK (0 errores)  
**Base de Datos:** ✅ Migraciones aplicadas (3/3)  
**Multitenancy:** ✅ Implementado en todas las vistas

---

## 🚀 Cómo Probar

### **Paso 0: Setup del Sistema (IMPORTANTE) ⚡**

Ejecuta el script de setup que crea todo automáticamente:

```powershell
cd d:\fronted SI2 web\web_si2\BackendLinux
.\venv\Scripts\python.exe setup_sistema.py
```

Este script automáticamente:
- ✅ Crea una empresa de prueba
- ✅ Crea superusuario (admin / admin123)
- ✅ Crea usuario normal (usuario1 / usuario123)
- ✅ Crea 4 tipos de crédito

**Resultado esperado:**
```
============================================================
✅ SETUP COMPLETADO
============================================================

📋 Credenciales para pruebas:
   Superusuario: admin / admin123
   Usuario normal: usuario1 / usuario123

🌐 Admin panel: http://127.0.0.1:8000/admin/
🎯 Aplicación: http://localhost:5173
```

---

### **Alternativa: Setup Manual**

Si prefieres hacerlo manualmente:

**1. Crear Empresa**
- Ir a http://127.0.0.1:8000/admin/
- Login con superusuario
- Empresas → Add Empresa
- Rellenar datos y guardar

**2. Crear Tipos de Crédito**
- Creditos → Tipo Creditos → Add Tipo Credito
- Crear al menos estos 4 tipos:
  - Préstamo Personal (1000 - 50000)
  - Crédito Vehicular (10000 - 200000)
  - Crédito Hipotecario (50000 - 500000)
  - Crédito Comercial (5000 - 300000)

**3. Asegúrate de seleccionar la empresa para cada tipo**

---

### **Paso 1: Iniciar el backend**

En **Terminal 1**:

```powershell
cd d:\fronted SI2 web\web_si2\BackendLinux
.\venv\Scripts\Activate.ps1
python manage.py runserver 8000
```

Verás:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### **Paso 2: Iniciar el frontend**

En **Terminal 2**:

```powershell
cd d:\fronted SI2 web\web_si2\FrontendGrupal
npm run dev
```

Verás:
```
VITE v5.x.x  ready in xx ms

➜  Local:   http://localhost:5173/
```

### **Paso 3: Abrir la aplicación**

Abre tu navegador y ve a: **http://localhost:5173**

Login con:
- **Usuario:** usuario1
- **Contraseña:** usuario123

---

## 🧪 Flujo de Prueba Completo

### **1️⃣ Crear un Cliente + Crédito**

1. **Login** con tus credenciales
2. Ir a **Clientes → Registrar Cliente + Crédito** (o directo a `/app/clientes/wizard`)
3. **Paso 1:** Ingresar datos del cliente (Nombre, Apellido, Teléfono)
   - Click **Siguiente**
4. **Paso 2:** Documentación
   - Ingresar CI y URL del documento
   - Click **Siguiente**
5. **Paso 3:** Información Laboral
   - Empresa, Puesto, Salario, etc.
   - Click **Siguiente**
6. **Paso 4:** Domicilio
   - Calle, Número, Apartamento, Zona
   - Click **Siguiente**
7. **Paso 5:** Seleccionar Tipo de Crédito
   - Elegir un tipo (Préstamo Personal, Vehicular, etc.)
   - Click **Siguiente**
8. **Paso 6:** Solicitar Crédito
   - Ingresar Monto, Tasa de Interés, Plazo
   - Click **Solicitar Crédito**

✅ **Resultado:** Deberías ver un banner verde: *"¡Crédito creado exitosamente!"*

### **2️⃣ Ver Crédito en la Lista**

Después de crear el crédito, automáticamente te redirige a `/app/creditos`

**Deberías ver:**

🎉 **BANNER AZUL** (en la parte superior):
```
┌─────────────────────────────────────────────┐
│ 🎉 ¡Crédito creado exitosamente!           │
│ Crédito #123 - Juan Pérez • $10,000 USD    │
│                                             │
│         [▶️ Continuar Workflow]             │
└─────────────────────────────────────────────┘
```

📊 **Estadísticas** (actualizadas)
- Total: 1
- Aprobados: 0
- En Proceso: 1
- Rechazados: 0

### **3️⃣ Ver el Workflow del Crédito**

**Click en el botón "▶️ Continuar Workflow"** en el banner azul

Se abrirá `/app/creditos/{id}/workflow` mostrando:

**Página del Workflow:**
- ✅ ID del crédito (ej: #123)
- ✅ Monto solicitado ($10,000 USD)
- ✅ **Fase Actual:** 📋 "Datos de la solicitud" (FASE_1)
- ✅ **Progreso:** 12.5% (1 de 8 fases completadas)

**Progreso Visual de Fases:**
- ✅ Fase 1: Datos de la solicitud - **COMPLETADO** ✓
- 🔵 Fase 2: Documentación personal - **EN PROGRESO**
- ⚪ Fases 3-8: Bloqueadas

**Datos Recopilados:**
- Monto Solicitado: $10,000
- Tasa de Interés: 10.5%
- Plazo: 12 meses
- Moneda: USD

---

## 🔑 Funcionalidades Incluidas

### **Backend (10 API Endpoints)**

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/api/creditos/` | POST | Crear crédito en FASE_1 |
| `/api/creditos/{id}/agregar-documentacion/` | PATCH | Pasar a FASE_2 |
| `/api/creditos/{id}/agregar-laboral/` | PATCH | Pasar a FASE_3 |
| `/api/creditos/{id}/agregar-domicilio/` | PATCH | Pasar a FASE_4 |
| `/api/creditos/{id}/agregar-garante/` | PATCH | Pasar a FASE_5 |
| `/api/creditos/{id}/enviar-revision/` | PATCH | Pasar a FASE_6 |
| `/api/creditos/{id}/revisar/` | PATCH | Pasar a FASE_7 o rechazar |
| `/api/creditos/{id}/desembolsar/` | PATCH | Pasar a FASE_8 |
| `/api/creditos/{id}/linea-tiempo/` | GET | Ver historial de cambios |
| `/api/creditos/{id}/estado-actual/` | GET | Ver fase actual y datos |

### **Frontend (Componentes)**

- ✅ **ClienteWizard** (6 pasos) - Crear cliente + crédito
- ✅ **CreditoWorkflowVisor** - Ver workflow del crédito
- ✅ **TimelineCredito** - Ver línea de tiempo (futuro)
- ✅ **WizardCredito** - Wizard de fases (futuro)

### **Base de Datos**

- ✅ **Modelo Credito** - 8 fases, campos de seguimiento
- ✅ **Modelo HistoricoCredito** - Auditoría completa
- ✅ **Multitenancy** - Filtrado por empresa

---

## 🐛 Verificar Multitenancy

### **Crear 2 Empresas y Probar Aislamiento**

1. Ir a **Empresas**
2. Crear **Empresa A** (ej: "Banco A")
3. Crear **Empresa B** (ej: "Banco B")
4. **Cambiar a Empresa A** en el selector de empresa
5. Crear un cliente + crédito
6. **Cambiar a Empresa B**
7. Ir a Créditos → **No deberías ver el crédito de Empresa A** ✅

---

## 📊 Verificar Workflow de Fases

1. Crear un crédito (queda en FASE_1)
2. Click en **"Continuar Workflow"**
3. Deberías ver:
   - ✅ FASE_1 completado (checkmark verde)
   - 🔵 FASE_2 en progreso (círculo azul)
   - ⚪ FASE_3-8 bloqueadas (círculos grises)
4. Progreso: **12.5%** (1 de 8 fases)

---

## 🔍 Ver Logs en Consola

### **Backend (Terminal)**
```
📤 [CREDITOS] POST /api/creditos/
📋 [CREDITOS] Datos a enviar: {...}
✅ [CREDITOS] Crédito creado exitosamente
```

### **Frontend (DevTools)**
```
Press F12 → Console
```

Verás logs como:
```
🔄 Cargando créditos desde el backend...
✅ Créditos cargados: 5
📤 Creando crédito: {...}
✅ Crédito creado: {...}
```

---

## ✅ Checklist de Prueba

- [ ] Ejecutar `python setup_sistema.py` exitosamente
- [ ] Backend inicia sin errores (puerto 8000)
- [ ] Frontend inicia sin errores (puerto 5173)
- [ ] Login con usuario1/usuario123 funciona
- [ ] Ver página de inicio y accesos rápidos
- [ ] Crear cliente en Paso 1
- [ ] Añadir documentación en Paso 2
- [ ] Información laboral en Paso 3
- [ ] Domicilio en Paso 4
- [ ] **Seleccionar tipo de crédito en Paso 5 (tipos creados por setup)**
- [ ] Crear crédito en Paso 6
- [ ] Ver banner "Crédito creado"
- [ ] Click en "Continuar Workflow"
- [ ] Ver FASE_1 completada (checkmark verde)
- [ ] Ver progreso 12.5%
- [ ] Datos recopilados mostrados correctamente
- [ ] Cambiar empresa → Crédito no visible (multitenancy)

---

## 💡 Próximos Pasos (Opcional)

1. **Conectar WizardCredito** a los endpoints PATCH para avanzar fases
2. **Implementar TimelineCredito** en la vista de workflow
3. **Agregar validaciones** en cada fase
4. **Pruebas end-to-end** de todo el flujo
5. **Pruebas de multitenancy** con 2+ empresas

---

## 🆘 Troubleshooting

**P: Backend no inicia**
```
❌ "Address already in use"
```
**R:** Cambia el puerto:
```powershell
python manage.py runserver 8001
```

**P: Frontend no ve el crédito creado**
```
❌ La lista de créditos no se actualiza
```
**R:** Backend tarda unos segundos. El frontend intenta recargar 3 veces automáticamente.

**P: Error en multitenancy**
```
❌ "No tienes acceso a esta empresa"
```
**R:** Asegúrate de estar logueado con un usuario de la empresa correcta.

---

¡Listo para probar! 🎉

