from .models import Credito, Tipo_Credito
from .serializers import CreditoSerializer, TipoCreditoSerializer
from app_User.models import Perfiluser
from rest_framework import viewsets, permissions


class TipoCreditoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoCreditoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Filtrar tipos de crédito por empresa del usuario"""
        user = self.request.user
        try:
            perfil = Perfiluser.objects.get(usuario=user)
            return Tipo_Credito.objects.filter(empresa=perfil.empresa)
        except Perfiluser.DoesNotExist:
            return Tipo_Credito.objects.none()
    
    def perform_create(self, serializer):
        """Auto-asignar empresa al crear tipo de crédito"""
        try:
            perfil = Perfiluser.objects.get(usuario=self.request.user)
            serializer.save(empresa=perfil.empresa)
        except Perfiluser.DoesNotExist:
            pass


class CreditoViewSet(viewsets.ModelViewSet):
    serializer_class = CreditoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            perfil = Perfiluser.objects.get(usuario=user)
            return Credito.objects.filter(empresa=perfil.empresa)
        except Perfiluser.DoesNotExist:
            return Credito.objects.none()

    def perform_create(self, serializer):
        try:
            perfil = Perfiluser.objects.get(usuario=self.request.user)
            serializer.save(empresa=perfil.empresa, usuario=self.request.user)
        except Perfiluser.DoesNotExist:
            pass
