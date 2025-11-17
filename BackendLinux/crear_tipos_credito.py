#!/usr/bin/env python
"""
Script para crear tipos de crédito por defecto en cada empresa
Uso: python manage.py shell < crear_tipos_credito.py
"""

from app_Credito.models import Tipo_Credito
from app_Empresa.models import Empresa

# Obtener todas las empresas
empresas = Empresa.objects.all()

if not empresas.exists():
    print("❌ No hay empresas. Crea una empresa primero.")
    exit(1)

# Tipos de crédito por defecto
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

# Crear tipos para cada empresa
for empresa in empresas:
    print(f"\n📦 Creando tipos de crédito para: {empresa.razon_social}")
    
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
            print(f"  ✅ Creado: {tipo.nombre}")
        else:
            print(f"  ⏭️  Ya existe: {tipo.nombre}")

print("\n✅ ¡Tipos de crédito configurados!")
print(f"\nTotal de tipos creados: {Tipo_Credito.objects.count()}")
for empresa in empresas:
    count = empresa.tipo_credito_set.count()
    print(f"  - {empresa.razon_social}: {count} tipos")
