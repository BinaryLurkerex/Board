
from django.urls import path, include #подключили новый метод
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('user', views.user, name='user'),
    path('modules', views.modules, name='modules'),
    path('status', views.status, name='status'),
    path('logout/', views.logout_view, name='logout'),
]
