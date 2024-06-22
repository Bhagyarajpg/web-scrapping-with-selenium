from django.contrib import admin
from django.urls import path
from wapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/save-entity/', views.save_entity, name='save_entity'),
    path('api/get-entity/', views.get_entity, name='get_entity'),
]