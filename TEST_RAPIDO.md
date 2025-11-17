# 🎯 TEST RÁPIDO - Continuar Workflow

## ⚡ 5 Minutos para Verificar

### **Paso 1: Reinicia el Frontend**

```powershell
# Terminal Frontend
Ctrl+C  # Detener npm run dev
npm run dev
```

Espera a ver:
```
➜  Local:   http://localhost:5173/
```

### **Paso 2: Crea un Cliente + Crédito**

1. Ve a http://localhost:5173/app/clientes/wizard
2. Completa los 6 pasos rápidamente
3. Click **"Solicitar Crédito"** en Paso 6
4. Espera 2 segundos a que redirija

### **Paso 3: Verifica el Banner**

**En la página de Créditos (http://localhost:5173/app/creditos)** deberías ver:

```
┌─────────────────────────────────────────┐
│ 🎉 ¡Crédito creado exitosamente!       │
│ Crédito #123 - Juan Pérez • $10,000 USD│
│                                         │
│     [▶️ Continuar Workflow]             │
└─────────────────────────────────────────┘

Total: 1  Aprobados: 0  En Proceso: 1  ...
```

### **Paso 4: Click en el Botón**

Click en **"▶️ Continuar Workflow"**

Deberías ver:
```
URL: http://localhost:5173/app/creditos/123/workflow

Contenido:
- 💳 Crédito #123
- 📊 Fase Actual: Datos de la solicitud
- 📈 Progreso: 12.5%
- 📋 Datos recopilados
- 8️⃣ Timeline de fases
```

---

## ✅ Si Todo Funciona

✅ Banner visible y bien formateado  
✅ Botón **"Continuar Workflow"** visible y funciona  
✅ Navega a `/app/creditos/{id}/workflow`  
✅ Ve la página del workflow correctamente  

¡Problema SOLUCIONADO! 🎉

---

## ❌ Si Algo Falla

### **Banner no se ve**
```
1. Abre DevTools (F12)
2. Console → Busca logs como "Créditos cargados: X"
3. Si dice 0, el backend no retorna créditos
4. Verifica: python manage.py runserver 8000
```

### **Botón no se ve**
```
1. Actualiza la página (Ctrl+F5)
2. Si sigue sin verse, el CSS no se aplicó
3. Revisa: npm run dev debe mostrar sin errores
```

### **Botón no funciona**
```
1. Abre DevTools → Console
2. Busca errores rojos
3. Click en botón y revisa URL en dirección
   Debe cambiar a: /app/creditos/123/workflow
```

---

¡A probar! 🚀

