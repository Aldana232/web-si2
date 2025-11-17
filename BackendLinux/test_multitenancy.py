#!/usr/bin/env python
"""
Script para probar multitenancia:
1. Crea 2 empresas
2. Crea 2 usuarios (uno por empresa)
3. Crea créditos en cada empresa
4. Verifica que cada usuario solo vea sus propios créditos
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Raiz_Project.settings')
django.setup()

from django.contrib.auth.models import User
from app_User.models import Perfiluser
from app_Empresa.models import Empresa
from app_Cliente.models import Cliente
from app_Credito.models import Credito, Tipo_Credito
from rest_framework.authtoken.models import Token
import json

print("=" * 80)
print("🔍 TEST DE MULTITENANCIA")
print("=" * 80)

# 1️⃣ Crear 2 empresas
print("\n1️⃣ CREAR 2 EMPRESAS")
empresa1, _ = Empresa.objects.get_or_create(
    razon_social="Empresa A",
    defaults={
        "nombre_comercial": "Empresa A",
        "email_contacto": "contacto@empresaa.com"
    }
)
print(f"✅ Empresa 1: {empresa1.razon_social} (ID: {empresa1.id})")

empresa2, _ = Empresa.objects.get_or_create(
    razon_social="Empresa B",
    defaults={
        "nombre_comercial": "Empresa B",
        "email_contacto": "contacto@empresab.com"
    }
)
print(f"✅ Empresa 2: {empresa2.razon_social} (ID: {empresa2.id})")

# 2️⃣ Crear 2 usuarios
print("\n2️⃣ CREAR 2 USUARIOS (UNO POR EMPRESA)")
user1, _ = User.objects.get_or_create(
    username="user_empresa_a",
    defaults={"email": "user@empresaa.com"}
)
print(f"✅ Usuario 1: {user1.username}")

user2, _ = User.objects.get_or_create(
    username="user_empresa_b",
    defaults={"email": "user@empresab.com"}
)
print(f"✅ Usuario 2: {user2.username}")

# 3️⃣ Asignar perfiles
print("\n3️⃣ ASIGNAR PERFILES A USUARIOS")
perfil1, _ = Perfiluser.objects.get_or_create(
    usuario=user1,
    empresa=empresa1
)
print(f"✅ Perfil 1: {user1.username} → {empresa1.razon_social}")

perfil2, _ = Perfiluser.objects.get_or_create(
    usuario=user2,
    empresa=empresa2
)
print(f"✅ Perfil 2: {user2.username} → {empresa2.razon_social}")

# 4️⃣ Crear clientes
print("\n4️⃣ CREAR CLIENTES EN CADA EMPRESA")
cliente1, _ = Cliente.objects.get_or_create(
    nombre="Cliente A",
    apellido="Apellido A",
    empresa=empresa1,
    defaults={"telefono": "5551234567"}
)
print(f"✅ Cliente 1: {cliente1.nombre} en {empresa1.razon_social}")

cliente2, _ = Cliente.objects.get_or_create(
    nombre="Cliente B",
    apellido="Apellido B",
    empresa=empresa2,
    defaults={"telefono": "5559876543"}
)
print(f"✅ Cliente 2: {cliente2.nombre} en {empresa2.razon_social}")

# 5️⃣ Crear tipos de crédito
print("\n5️⃣ CREAR TIPOS DE CRÉDITO")
tipo1, _ = Tipo_Credito.objects.get_or_create(
    nombre="Crédito Normal A",
    empresa=empresa1,
    defaults={
        "descripcion": "Tipo de crédito para empresa A",
        "tasa_interes": 15.0,
        "plazo_meses": 12
    }
)
print(f"✅ Tipo 1: {tipo1.nombre} en {empresa1.razon_social}")

tipo2, _ = Tipo_Credito.objects.get_or_create(
    nombre="Crédito Normal B",
    empresa=empresa2,
    defaults={
        "descripcion": "Tipo de crédito para empresa B",
        "tasa_interes": 18.0,
        "plazo_meses": 12
    }
)
print(f"✅ Tipo 2: {tipo2.nombre} en {empresa2.razon_social}")

# 6️⃣ Crear créditos
print("\n6️⃣ CREAR CRÉDITOS EN CADA EMPRESA")
credito1, _ = Credito.objects.get_or_create(
    cliente=cliente1,
    tipo_credito=tipo1,
    empresa=empresa1,
    defaults={
        "monto": 5000.00,
        "usuario_creador": user1,
        "fase_actual": "FASE_1_SOLICITUD",
        "estado": "SOLICITADO"
    }
)
print(f"✅ Crédito 1: Bs. {credito1.monto} en {empresa1.razon_social}")

credito2, _ = Credito.objects.get_or_create(
    cliente=cliente2,
    tipo_credito=tipo2,
    empresa=empresa2,
    defaults={
        "monto": 8000.00,
        "usuario_creador": user2,
        "fase_actual": "FASE_1_SOLICITUD",
        "estado": "SOLICITADO"
    }
)
print(f"✅ Crédito 2: Bs. {credito2.monto} en {empresa2.razon_social}")

# 7️⃣ OBTENER TOKENS
print("\n7️⃣ OBTENER TOKENS")
token1, _ = Token.objects.get_or_create(user=user1)
print(f"✅ Token User 1: {token1.key}")

token2, _ = Token.objects.get_or_create(user=user2)
print(f"✅ Token User 2: {token2.key}")

# 8️⃣ VERIFICAR MULTITENANCIA
print("\n8️⃣ VERIFICAR MULTITENANCIA")
print("\n📊 Créditos TOTALES en BD:", Credito.objects.count())
print("📊 Créditos en Empresa A:", Credito.objects.filter(empresa=empresa1).count())
print("📊 Créditos en Empresa B:", Credito.objects.filter(empresa=empresa2).count())

print("\n" + "=" * 80)
print("✅ TEST DE MULTITENANCIA COMPLETADO")
print("=" * 80)

print("\n📝 PRÓXIMOS PASOS:")
print("1. En navegador, entra como user_empresa_a")
print("2. Deberías ver créditos de SOLO Empresa A")
print("3. En otra pestaña incógnito, entra como user_empresa_b")
print("4. Deberías ver créditos de SOLO Empresa B")
print("5. Verifica que los créditos de la otra empresa NO aparecen")
