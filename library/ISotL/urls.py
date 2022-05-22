from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ISotL.views import BooksViewSet, UserViewSet

simple_router = SimpleRouter()
simple_router.register(r"books", BooksViewSet)
simple_router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(simple_router.urls)),
    path('auth/', include('djoser.urls'))
]
