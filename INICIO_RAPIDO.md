# 🎯 GUÍA RÁPIDA DE INICIO

## ⏱️ 5 Minutos para Tener Todo Funcionando

### Paso 1️⃣: Setup del Sistema (2 min)

```powershell
cd BackendLinux
.\venv\Scripts\Activate.ps1
python setup_sistema.py
```

✅ Esto crea:
- 📦 Empresa de prueba
- 👤 Superusuario: admin / admin123
- 👤 Usuario normal: usuario1 / usuario123
- 💳 4 tipos de crédito listos para usar

### Paso 2️⃣: Iniciar Backend (1 min)

```powershell
# Terminal 1
cd BackendLinux
python manage.py runserver 8000
```

Espera a ver:
```
Starting development server at http://127.0.0.1:8000/
```

### Paso 3️⃣: Iniciar Frontend (1 min)

```powershell
# Terminal 2
cd FrontendGrupal
npm run dev
```

Espera a ver:
```
➜  Local:   http://localhost:5173/
```

### Paso 4️⃣: Abrir Aplicación (1 min)

1. Abre http://localhost:5173
2. Login:
   - Usuario: **usuario1**
   - Contraseña: **usuario123**

---

## ✅ Verificar que Funciona

### 1️⃣ Ver Tipos de Crédito
**URL:** http://127.0.0.1:8000/api/Creditos/test/tipos/

Deberías ver JSON con 4 tipos de crédito:
```json
{
  "success": true,
  "empresa": "Banco Prueba",
  "tipos_credito": [
    {"id": 1, "nombre": "Préstamo Personal", ...},
    {"id": 2, "nombre": "Crédito Vehicular", ...},
    ...
  ],
  "total": 4
}
```

### 2️⃣ Crear Cliente + Crédito
1. Click en **"Registrar Cliente + Crédito"**
2. **Paso 1-5:** Rellenar datos
3. **Paso 6:** Crear crédito
4. ✅ Ver banner azul: "¡Crédito creado exitosamente!"

### 3️⃣ Ver Workflow
1. Click en **"Continuar Workflow"** en el banner
2. Ver:
   - 💳 ID del crédito
   - 📊 Fase actual: "Datos de la solicitud" (FASE_1)
   - 📈 Progreso: 12.5%
   - 📋 Datos recopilados

---

## 🌐 URLs Importantes

| URL | Propósito |
|-----|-----------|
| http://127.0.0.1:8000/admin/ | Admin de Django |
| http://127.0.0.1:8000/api/Creditos/tipo-creditos/ | Tipos de crédito (API) |
| http://127.0.0.1:8000/api/Creditos/creditos/ | Créditos (API) |
| http://localhost:5173/app/clientes/wizard | Wizard cliente+crédito |
| http://localhost:5173/app/creditos | Lista de créditos |

---

## 🐛 Si Algo No Funciona

### "AttributeError: No module named 'app_Credito'"
```powershell
cd BackendLinux
python manage.py migrate
```

### "Port already in use"
```powershell
# Usa otro puerto
python manage.py runserver 8001
```

### "No types found when selecting credit type"
```powershell
# Ejecuta setup de nuevo
python setup_sistema.py
```

### TypeScript errors en frontend
```powershell
cd FrontendGrupal
npm install
npm run dev
```

---

## 📱 Flujo de Prueba (5 min)

```
1. Login ← usuario1/usuario123
        ↓
2. Clientes → Registrar Cliente
        ↓
3. Paso 1: Datos cliente (nombre, apellido, teléfono)
        ↓
4. Paso 2: Documentación (CI, documento)
        ↓
5. Paso 3: Trabajo (empresa, puesto, salario)
        ↓
6. Paso 4: Domicilio (dirección)
        ↓
7. Paso 5: Seleccionar tipo de crédito ← (creado por setup)
        ↓
8. Paso 6: Crear crédito (monto, tasa, plazo)
        ↓
9. ✅ Banner: "¡Crédito creado!"
        ↓
10. Click: "Continuar Workflow"
        ↓
11. Ver: Workflow del crédito en FASE_1
```

---

## ✨ Características Implementadas

✅ Multitenancy: Cada empresa ve solo sus datos  
✅ 8 Fases: Desde solicitud hasta finalización  
✅ Auditoría: Historial completo de cambios  
✅ Validaciones: En cada etapa del proceso  
✅ UI Responsiva: Funciona en mobile y desktop  

---

## 📚 Documentación Completa

- `GUIA_PRUEBA_SISTEMA.md` - Guía de prueba detallada
- `BackendLinux/QUICKSTART.md` - Quick start del backend
- `RESUMEN_IMPLEMENTACION.md` - Resumen técnico

---

¡Estás listo para probar! 🚀

Cualquier problema, revisa la carpeta `docs/` o los logs del backend.

