from rest_framework.authentication import BasicAuthentication
from rest_framework.viewsets import ModelViewSet

from .models import Books, User
from .permission import *
from .serializers import BooksSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdmin]
        elif self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
class BooksViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdmin]
        elif self.action == 'list':
            permission_classes = [IsAdminOrManagerOrGuest]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsManagerOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
