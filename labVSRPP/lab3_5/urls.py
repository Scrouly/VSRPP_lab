from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from lab3_5 import views
from lab3_5.views import StudentsViewSet, GroupsViewSet, FacultyViewSet

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user-list')
router.register('login', views.LoginView, basename='login')

simple_router = SimpleRouter()
simple_router.register(r"students", StudentsViewSet)
simple_router.register(r"groups", GroupsViewSet)
simple_router.register(r"faculty", FacultyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include(simple_router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
