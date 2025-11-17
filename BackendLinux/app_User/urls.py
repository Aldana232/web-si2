from django.urls import include, path
from rest_framework import routers
from .api_user import UserViewSer, GroupViewSet, PermissionViewSer, ContentTypeViewSer, AdminLogViewSet, CreateUserView


router = routers.DefaultRouter()
router.register(r'user', UserViewSer, basename='user')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'permission', PermissionViewSer, basename='permission')
router.register(r'content-type', ContentTypeViewSer, basename='content-type')
router.register(r'admin-log', AdminLogViewSet, basename='admin-log')

urlpatterns = [
    path('', include(router.urls)),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
]