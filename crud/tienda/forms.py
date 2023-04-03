from django import forms

class BuscarProductoForm(forms.Form):
    criterio_nombre=forms.CharField(max_length=100)

class BuscarHeroeForm(forms.Form):
    heroe_nombre=forms.CharField(max_length=100)

class BuscarUsuarioForm(forms.Form):
    usuario_alias=forms.CharField(max_length=100)

