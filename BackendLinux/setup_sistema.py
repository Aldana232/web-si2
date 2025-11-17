#!/usr/bin/env python
"""
Script de Setup Completo
Ejecutar: python setup_sistema.py

Este script:
1. Crea una empresa de prueba
2. Crea un superusuario
3. Crea un usuario normal
4. Crea tipos de crédito por defecto
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Raiz_Project.settings')
django.setup()

from django.contrib.auth.models import User
from app_Empresa.models import Empresa
from app_User.models import Perfiluser
from app_Credito.models import Tipo_Credito

def crear_empresa():
    """Crear empresa de prueba si no existe"""
    empresa, created = Empresa.objects.get_or_create(
        razon_social='Banco Prueba',
        defaults={
            'ruc': '1234567890',
            'direccion': 'Calle Principal 123',
            'telefono': '+591 2 1234567',
            'email': 'info@banco-prueba.com'
        }
    )
    
    if created:
        print(f"✅ Empresa creada: {empresa.razon_social}")
    else:
        print(f"⏭️  Empresa ya existe: {empresa.razon_social}")
    
    return empresa

def crear_superusuario(empresa):
    """Crear superusuario si no existe"""
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@banco-prueba.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    
    if created:
        user.set_password('admin123')
        user.save()
        print(f"✅ Superusuario creado: admin / admin123")
    else:
        print(f"⏭️  Superusuario ya existe: admin")
    
    # Crear perfil si no existe
    perfil, created = Perfiluser.objects.get_or_create(
        usuario=user,
        defaults={
            'empresa': empresa,
            'rol': 'admin'
        }
    )
    
    if created:
        print(f"✅ Perfil de admin creado")
    
    return user

def crear_usuario_normal(empresa):
    """Crear usuario normal para pruebas"""
    user, created = User.objects.get_or_create(
        username='usuario1',
        defaults={
            'email': 'usuario1@banco-prueba.com',
            'is_staff': False,
            'is_superuser': False
        }
    )
    
    if created:
        user.set_password('usuario123')
        user.save()
        print(f"✅ Usuario normal creado: usuario1 / usuario123")
    else:
        print(f"⏭️  Usuario normal ya existe: usuario1")
    
    # Crear perfil si no existe
    perfil, created = Perfiluser.objects.get_or_create(
        usuario=user,
        defaults={
            'empresa': empresa,
            'rol': 'user'
        }
    )
    
    if created:
        print(f"✅ Perfil de usuario normal creado")
    
    return user

def crear_tipos_credito(empresa):
    """Crear tipos de crédito por defecto"""
    tipos_default = [
        {
            'nombre': 'Préstamo Personal',
            'descripcion': 'Préstamo sin garantía para gastos personales',
            'monto_minimo': 1000,
            'monto_maximo': 50000
        },
        {
            'nombre': 'Crédito Vehicular',
            'descripcion': 'Financiamiento para compra de vehículos',
            'monto_minimo': 10000,
            'monto_maximo': 200000
        },
        {
            'nombre': 'Crédito Hipotecario',
            'descripcion': 'Financiamiento para compra de vivienda',
            'monto_minimo': 50000,
            'monto_maximo': 500000
        },
        {
            'nombre': 'Crédito Comercial',
            'descripcion': 'Financiamiento para actividades comerciales',
            'monto_minimo': 5000,
            'monto_maximo': 300000
        },
    ]
    
    print("\n📦 Creando tipos de crédito para:", empresa.razon_social)
    
    for tipo_data in tipos_default:
        tipo, created = Tipo_Credito.objects.get_or_create(
            nombre=tipo_data['nombre'],
            empresa=empresa,
            defaults={
                'descripcion': tipo_data['descripcion'],
                'monto_minimo': tipo_data['monto_minimo'],
                'monto_maximo': tipo_data['monto_maximo'],
            }
        )
        
        if created:
            print(f"  ✅ {tipo.nombre}")
        else:
            print(f"  ⏭️  {tipo.nombre} (ya existe)")

def main():
    print("\n" + "="*60)
    print("🚀 SETUP SISTEMA - Preparando ambiente para pruebas")
    print("="*60 + "\n")
    
    try:
        # 1. Crear empresa
        empresa = crear_empresa()
        
        # 2. Crear superusuario
        print("\n👤 Configurando superusuario...")
        crear_superusuario(empresa)
        
        # 3. Crear usuario normal
        print("\n👤 Configurando usuario normal...")
        crear_usuario_normal(empresa)
        
        # 4. Crear tipos de crédito
        crear_tipos_credito(empresa)
        
        print("\n" + "="*60)
        print("✅ SETUP COMPLETADO")
        print("="*60)
        print("\n📋 Credenciales para pruebas:")
        print("   Superusuario: admin / admin123")
        print("   Usuario normal: usuario1 / usuario123")
        print("\n🌐 Admin panel: http://127.0.0.1:8000/admin/")
        print("🎯 Aplicación: http://localhost:5173")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error durante el setup: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
