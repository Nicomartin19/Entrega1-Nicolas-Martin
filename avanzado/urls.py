from django.urls import path
from avanzado import views

urlpatterns=[
    #Version con vistas comunes
    # path("mascotas/", views.ver_mascotas, name="ver_mascotas"),
    path("mascotas/crear/", views.crear_mascota, name="crear_mascota"),
    # path("mascotas/editar/<int:id>", views.editar_mascota, name="editar_mascota"),
    # path("mascotas/eliminar/<int:id>", views.eliminar_mascota, name="eliminar_mascota"),
    
    # Version con clases basadas en vistas.
    path("mascotas/", views.ListaMascota.as_view(), name="ver_mascotas"),
    # path("mascotas/crear/", views.CrearMascota.as_view(), name="crear_mascota"),
    path("mascotas/editar/<int:pk>", views.EditarMascota.as_view(), name="editar_mascota"),
    path("mascotas/eliminar/<int:pk>", views.EliminarMascota.as_view(), name="eliminar_mascota"),
    path("mascotas/ver/<int:pk>", views.VerMascota.as_view(), name="ver_mascota"),
    
    
]