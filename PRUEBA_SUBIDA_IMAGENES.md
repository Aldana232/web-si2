# PRUEBA RÁPIDA - VERIFICAR SUBIDA DE IMÁGENES A S3

## Estado Actual del Sistema

✅ **Conexión S3 funcionando**: El test simple confirmó que:
- Las credenciales AWS son correctas
- El bucket `byvagners3` es accesible  
- Se pueden subir archivos correctamente
- Archivo de prueba subido: `test/prueba_upload.txt`

❌ **Problema**: Los archivos NO llegan desde el frontend al backend

## Pasos para Diagnóstico

### 1. Verificar que el navegador tiene los archivos

Abre la página de registro y:
1. Sube una imagen de empresa
2. Suba una imagen de usuario
3. Abre la consola del navegador (F12)
4. Busca estos mensajes en la consola:

```
[confirmación] 🔍 Verificando archivos:
[confirmación] companyLogoFile: ✅ nombre_archivo.jpg (12345 bytes)
[confirmación] userAvatarFile: ✅ nombre_archivo.png (54321 bytes)
```

Si ves ❌ null en lugar de ✅ con el nombre del archivo, significa que los archivos se están perdiendo antes de crear el FormData.

### 2. Verificar el FormData

Después de crear el FormData, deberías ver:

```
[confirmación] 📦 FormData preparado. Contenido:
  - imagen_empresa: [File] nombre.jpg (12345 bytes, image/jpeg)
  - imagen_perfil: [File] nombre.png (54321 bytes, image/png)
```

### 3. Verificar que se envía como multipart/form-data

En service.ts deberías ver:

```
[auth] payload es FormData: true
[auth] 📦 Contenido del FormData:
[auth]   - imagen_empresa: [File] nombre.jpg (12345 bytes, image/jpeg)
[auth]   - imagen_perfil: [File] nombre.png (54321 bytes, image/png)
```

### 4. Verificar en el backend

En la terminal del backend (donde corre Django) deberías ver:

```
🔍 [RegisterEmpresa] Content-Type: multipart/form-data; boundary=...
📥 [RegisterEmpresa] FILES recibidos: ['imagen_empresa', 'imagen_perfil']
🖼️ [RegisterEmpresa] Imagen empresa: nombre.jpg
🖼️ [RegisterEmpresa] Imagen perfil: nombre.png
```

## Posibles Problemas y Soluciones

### Problema A: Archivos null en handleConfirmRegistration
**Síntoma**: `companyLogoFile: ❌ null`

**Causa**: Los archivos se están perdiendo cuando se abre el modal.

**Solución**: Guardar los archivos en `preparedRegistrationData` antes de abrir el modal.

### Problema B: FormData no contiene archivos
**Síntoma**: FormData solo tiene campos de texto

**Causa**: Los archivos no se están agregando correctamente al FormData.

**Solución**: Verificar que `companyLogoFile` y `userAvatarFile` no sean null.

### Problema C: Backend recibe application/json
**Síntoma**: `Content-Type: application/json` en vez de `multipart/form-data`

**Causa**: Axios o un interceptor está convirtiendo FormData a JSON.

**Solución**: NO establecer Content-Type manualmente, dejar que Axios lo maneje.

### Problema D: Backend no recibe archivos en request.FILES
**Síntoma**: `FILES recibidos: []` (lista vacía)

**Causa**: Django no está parseando el multipart/form-data correctamente.

**Solución**: Verificar que la API tenga `MultiPartParser` en parser_classes.

## Ejecutar Prueba

1. **Frontend**:
   ```bash
   cd FrontendGrupal
   npm run dev
   ```

2. **Backend**:
   ```bash
   cd BackendLinux
   python manage.py runserver
   ```

3. **Navega a**: http://localhost:5173 (o el puerto donde corre tu frontend)

4. **Completa el formulario** de registro con ambas imágenes

5. **Observa la consola** del navegador y del backend

6. **Reporta qué paso falla** según la información arriba

## Resultado Esperado

Si todo funciona:
- ✅ Consola frontend: archivos detectados y en FormData
- ✅ Consola backend: archivos recibidos en request.FILES
- ✅ Archivos aparecen en S3 bucket en las carpetas:
  * `empresas/logos/`
  * `usuarios/avatars/`
- ✅ Database muestra URLs completas en lugar de [null]

## Siguiente Paso

Una vez que identifiques en qué paso falla, avísame y ajustaremos el código específico.
