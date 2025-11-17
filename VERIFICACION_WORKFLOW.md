# ✅ Verificación - Workflow de Crédito

## 🎯 Qué Deberías Ver Paso a Paso

### **PASO 1: Crear Cliente + Crédito**

**URL:** http://localhost:5173/app/clientes/wizard

```
┌─────────────────────────────────────┐
│ 🎯 Wizard de Cliente + Crédito      │
├─────────────────────────────────────┤
│                                     │
│  Paso 1: Datos Cliente          [✓] │
│  Paso 2: Documentación          [ ] │
│  Paso 3: Trabajo                [ ] │
│  Paso 4: Domicilio              [ ] │
│  Paso 5: Tipo de Crédito        [ ] │
│  Paso 6: Crear Crédito          [ ] │
│                                     │
│  Formulario:                        │
│  - Nombre: [____________]           │
│  - Apellido: [____________]         │
│  - Teléfono: [____________]         │
│                                     │
│                    [← Atrás] [Next →│
└─────────────────────────────────────┘
```

**Completa todos los 6 pasos**

---

### **PASO 2: Crédito Creado - Banner**

**URL:** http://localhost:5173/app/creditos

**Deberías VER:**

```
┌────────────────────────────────────────────────────────────┐
│                    PÁGINA DE CRÉDITOS                       │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  🎉 ¡Crédito creado exitosamente!                   │ │
│  │  Crédito #123 - Juan Pérez • $10,000 USD            │ │
│  │                          [▶️ Continuar Workflow]     │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌──────────┬──────────┬──────────┬──────────┐            │
│  │ Total: 5 │Aprobados:│ En Proceso:│Rechazados│            │
│  │ Créditos │  2       │   3       │  0       │            │
│  └──────────┴──────────┴──────────┴──────────┘            │
│                                                             │
│  [🔄 Actualizar Lista] [🔍 Buscar]  [👁️ Ver Todos]        │
│                                                             │
│  TABLA DE CRÉDITOS:                                        │
│  ┌─────┬──────────┬─────────┬──────────┬─────────────┐    │
│  │ ID  │ Cliente  │ Monto   │ Estado   │ Acciones    │    │
│  ├─────┼──────────┼─────────┼──────────┼─────────────┤    │
│  │ 123 │ Juan P.  │ $10,000 │SOLICITADO│ [Ver] [Editar│    │
│  └─────┴──────────┴─────────┴──────────┴─────────────┘    │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

**Si NO ves el banner azul:**
- ❌ El crédito no se creó exitosamente (revisa logs)
- ❌ No se pudo obtener la lista de créditos
- ❌ El redirect no funcionó

---

### **PASO 3: Click en "▶️ Continuar Workflow"**

**URL:** http://localhost:5173/app/creditos/123/workflow

**Deberías VER:**

```
┌────────────────────────────────────────────────────────────┐
│              💳 WORKFLOW DEL CRÉDITO #123                   │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  💳 Crédito #123                           $10,000 USD     │
│  Cliente ID: 5                                              │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ 🎯 FASE ACTUAL                                       │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │  📋 Datos de la solicitud                            │ │
│  │  Progreso: 12.5% (1 de 8 fases)                     │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ 📊 PROGRESO DEL FLUJO                               │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │ ① ✓ Datos de la solicitud      [COMPLETADO]        │ │
│  │ ② 🔵 Documentación personal    [EN PROGRESO]       │ │
│  │ ③ ⚪ Información laboral        [BLOQUEADO]         │ │
│  │ ④ ⚪ Domicilio                  [BLOQUEADO]         │ │
│  │ ⑤ ⚪ Datos del garante         [BLOQUEADO]         │ │
│  │ ⑥ ⚪ Revisión y aprobación      [BLOQUEADO]         │ │
│  │ ⑦ ⚪ Desembolso del crédito     [BLOQUEADO]         │ │
│  │ ⑧ ⚪ Crédito finalizado        [BLOQUEADO]         │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ 📋 DATOS RECOPILADOS                                │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │ Monto Solicitado: $10,000                           │ │
│  │ Tasa de Interés: 10.5%                              │ │
│  │ Plazo: 12 meses                                     │ │
│  │ Moneda: USD                                         │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                             │
│               [← Volver]        [▶️ Continuar Workflow]    │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## ✅ Checklist de Verificación

### **Backend**
- [ ] `python setup_sistema.py` ejecutado sin errores
- [ ] `python manage.py runserver 8000` corriendo
- [ ] Logs muestran: `Starting development server...`

### **Frontend**
- [ ] `npm run dev` corriendo
- [ ] Logs muestran: `Local: http://localhost:5173/`
- [ ] No hay errores en la consola (F12)

### **Login**
- [ ] Login exitoso con usuario1/usuario123
- [ ] Dashboard visible

### **Crear Crédito**
- [ ] Wizard de 6 pasos accesible
- [ ] Cada paso acepta datos
- [ ] Paso 5 muestra tipos de crédito (al menos 4)
- [ ] Click en "Solicitar Crédito" en Paso 6
- [ ] Redirección a `/app/creditos` (sin error)

### **Ver Workflow**
- [ ] ✅ Banner azul "¡Crédito creado exitosamente!" visible
- [ ] ✅ Botón "▶️ Continuar Workflow" presente
- [ ] ✅ Click abre `/app/creditos/{id}/workflow`
- [ ] ✅ Página muestra:
  - [ ] ID del crédito
  - [ ] Monto solicitado
  - [ ] 📋 FASE ACTUAL (Datos de la solicitud)
  - [ ] Progreso: 12.5%
  - [ ] 📊 8 fases con checkmarks verdes/azules/grises
  - [ ] Datos recopilados (Monto, Tasa, Plazo, Moneda)

---

## 🐛 Si NO Ves el Banner

### **Problema 1: No ves el banner azul**

**Causas posibles:**
1. El crédito NO se creó (revisa logs del backend)
2. El redirect no funcionó (historial no recargó)
3. El backend devuelve error 500

**Solución:**
```powershell
# Terminal 1 (Backend)
# Revisa los logs para ver si hay errores

# En otra terminal, prueba crear tipo de crédito directamente
curl -X GET http://127.0.0.1:8000/api/Creditos/test/tipos/ \
  -H "Authorization: Token TU_TOKEN"
```

### **Problema 2: El banner aparece pero botón no funciona**

**Causas posibles:**
1. El ID del crédito es 0 o inválido
2. La ruta `/app/creditos/{id}/workflow` no existe
3. El componente CreditoWorkflowVisor no renderiza

**Solución:**
```
1. Revisa en DevTools (F12) → Network
2. Busca llamadas a `/api/creditos/`
3. Verifica que devuelva `id` y `Monto_Solicitado`
4. Click en botón y revisa URL en direcciónn
```

### **Problema 3: Página en blanco o error 404**

**Causas posibles:**
1. CreditoWorkflowVisor no está importado en main.tsx
2. Ruta no está configurada
3. getCreditoById() falla

**Solución:**
```powershell
# Verifica en DevTools Console
# Deberías ver:
# 📤 [CREDITOS] GET /api/creditos/123/
# ✅ [CREDITOS] Crédito obtenido...
```

---

## 🔍 Cómo Verificar en DevTools

### **Console (F12)**
```javascript
// Ver créditos en memoria
console.log('Ver historial')

// Hacer petición directa
fetch('/api/Creditos/creditos/', {
  headers: { 'Authorization': 'Token TU_TOKEN' }
})
.then(r => r.json())
.then(d => console.log(d))
```

### **Network Tab**
```
1. Crear crédito → busca POST /api/Creditos/creditos/
   - Status: 201 (OK)
   - Response: JSON con id del crédito

2. Recargar página → busca GET /api/Creditos/creditos/
   - Status: 200 (OK)
   - Response: Array con créditos
```

---

## ✨ Todo Debe Funcionar

Si seguiste los pasos:

1. ✅ **Setup:** `python setup_sistema.py`
2. ✅ **Backend:** `python manage.py runserver 8000`
3. ✅ **Frontend:** `npm run dev`
4. ✅ **Login:** usuario1 / usuario123
5. ✅ **Crear crédito:** 6 pasos
6. ✅ **Ver workflow:** Banner + botón + página

Deberías ver **EXACTAMENTE** lo que se muestra arriba.

Si no lo ves, **revisa los logs** de backend y frontend. 🔧

