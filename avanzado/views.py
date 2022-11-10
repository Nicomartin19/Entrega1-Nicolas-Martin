from contextlib import redirect_stderr
from doctest import DONT_ACCEPT_BLANKLINE
from pyexpat import model
from statistics import mode
from django.shortcuts import redirect, render
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario, BusquedaMascota

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
# def ver_mascotas(request):
    
#     mascotas = Mascota.objects.all()
    
#     return render(request, "avanzado/ver_mascotas.html", {"mascotas": mascotas})

@login_required
def crear_mascota(request):
    
    if request.method == "POST":
        formulario = MascotaFormulario(request.POST)
        
        
        if formulario.is_valid():
            datos = formulario.cleaned_data

            mascota = Mascota(
            nombre=datos["nombre"], 
            tipo=datos["tipo"], 
            edad=datos["edad"],
            fecha_nacimiento=datos["fecha_nacimiento"],
           
            )
            mascota.save()
            return redirect("ver_mascotas")
        else:
             return render(request, "avanzado/crear_mascota.html", {"formulario": formulario})
        
    formulario = MascotaFormulario()
        
    return render(request, "avanzado/crear_mascota.html", {"formulario": formulario})

def editar_mascota(request, id):
    mascota= Mascota.objects.get(id=id)
    
    if request.method == "POST":
        formulario = MascotaFormulario(request.POST)
        
        
        if formulario.is_valid():
            datos = formulario.cleaned_data

            mascota.nombre = datos["nombre"]
            mascota.tipo = datos["tipo"]
            mascota.edad = datos["edad"]
            mascota.fecha_nacimiento = datos["fecha_nacimiento"]
            
            mascota.save()
            return redirect("ver_mascotas")
        else:
            return render(request, "avanzado/editar_mascota.html", {"formulario": formulario, "mascota": mascota})
        
    formulario = MascotaFormulario(
        initial={
            "nombre": mascota.nombre, 
            "tipo": mascota.tipo, 
            "edad": mascota.edad, 
            "fecha_nacimiento": mascota.fecha_nacimiento
        })
        
    return render(request, "avanzado/editar_mascota.html", {"formulario": formulario, "mascota": mascota})

def eliminar_mascota(request, id):
    
    mascota= Mascota.objects.get(id=id)
    
    mascota.delete()
    
    return redirect("ver_mascotas")

class ListaMascota(ListView):
    model = Mascota
    template_name = "avanzado/ver_mascotas_cbv.html"
    
    def get_queryset(self):
        nombre = self.request.GET.get("nombre", "")
        if nombre:
            object_list = self.model.objects.filter(nombre=nombre)
        else: 
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["formulario"] = BusquedaMascota()
        return context
    
class CrearMascota(CreateView):
    model = Mascota
    success_url = "/avanzado/mascotas/"
    template_name = "avanzado/crear_mascota_cbv.html"
    fields = ["nombre", "tipo", "edad", "fecha_nacimiento", "descripcion"]
    

class EditarMascota(LoginRequiredMixin, UpdateView):
    model = Mascota
    success_url = "/avanzado/mascotas/"
    template_name = "avanzado/editar_mascota_cbv.html"
    fields = ["nombre", "tipo", "edad", "fecha_nacimiento", "descripcion"]
    
class EliminarMascota(LoginRequiredMixin, DeleteView):
    model = Mascota
    success_url = "/avanzado/mascotas/"
    template_name = "avanzado/eliminar_mascota_cbv.html"
    
    
    
class VerMascota(DetailView):
    model = Mascota
    template_name = "avanzado/ver_mascota.html"
    
    