from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from accounts.forms import MiFormularioDeCreacion, EditarPerfilFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import ExtensionUsuario
 
def mi_login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect("index")
        
    else:
        formulario = AuthenticationForm()
    
    
    return render(request, "accounts/login.html", {"formulario": formulario})

def registrar(request):
    
    if request.method == "POST":
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("index")
    else:
        
        formulario = MiFormularioDeCreacion()
    
    
    return render(request, "accounts/registrar.html", {"formulario": formulario})

@login_required
def perfil(request):
   
    return render(request, "accounts/perfil.html", {})

@login_required
def editar_perfil(request):
    user = request.user
   
    
    if request.method == "POST":
       formulario = EditarPerfilFormulario(request.POST, request.FILES)
       
       if formulario.is_valid():
           data_nueva = formulario.cleaned_data
           user.first_name = data_nueva["first_name"] 
           user.last_name = data_nueva["last_name"]
           user.email = data_nueva["email"]
           user.extensionusuario.avatar = data_nueva["avatar"]
           
          
           
           user.extensionusuario.save()
           user.save()
           
           return redirect("perfil")
    else:
        formulario = EditarPerfilFormulario(
            initial={
                "first_name": user.first_name, 
                "last_name": user.last_name, 
                "email": user.email,
                "avatar": user.extensionusuario.avatar,
                
                
                
            }
        )
    
    return render(request, "accounts/editar_perfil.html", {"formulario": formulario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/cambiar_contraseña.html"
    success_url = "/accounts/perfil/"
    
    
