from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hola/", views.hola, name="hola"),
    path("fecha/", views.fecha, name="fecha"),
    path("fecha-nacimiento/<int:edad>", views.calcular_fecha_nacimiento),
    # path("mi-template/", views.mi_temple, name="mi_template"),
    path("mi-template/<str:nombre>", views.tu_temple),
    path("prueba-template/", views.prueba_template),
    path("ver-personas/", views.ver_personas, name="ver_personas"),
    path("crear-persona/", views.crear_persona, name="crear_persona"),
<<<<<<< HEAD
    
]
=======
    path("nosotros/", views.nosotros, name="nosotros"),
]
>>>>>>> 1775887b9ee18e3a3f5c69e44ddebe5f90805f1b
