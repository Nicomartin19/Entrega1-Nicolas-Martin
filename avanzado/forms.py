from django import forms
from ckeditor.fields import RichTextFormField

class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    tipo = forms.CharField(max_length = 20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    descripcion = RichTextFormField(required=False)
    
    
class BusquedaMascota(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
