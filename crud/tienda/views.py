from django.shortcuts import render, redirect
from tienda.models import Producto, Heroe, Usuario
from django.contrib import messages
from django.views.generic import ListView
from tienda.forms import BuscarProductoForm, BuscarHeroeForm, BuscarUsuarioForm
from .models import Heroe
from .forms import BuscarHeroeForm




# Create your views here.

def home(request):
    return render(request,"principal.html")

def consultar(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {
        'productos' : productos
    })    

def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    p = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    p.save()
    messages.success(request, 'Producto agregado')
    return redirect('consultar')

def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, 'Producto eliminado')
    return redirect('consultar')

def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, "productoEditar.html",{
        'producto' : producto
    })    

def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    id = request.POST["id"]
    Producto.objects.filter(pk=id).update(id=id,nombre=nombre,precio=precio,descripcion=descripcion) 
    messages.success(request, 'Producto actualizado')
    return redirect('consultar')

class BuscarProducto(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = "productos"

    def get_queryset(self):
        f = BuscarProductoForm(self.request.GET)
        if f.is_valid():
            return Producto.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Producto.objects.none()





def consultar1(request):
    heroe = Heroe.objects.all()
    return render(request, "heroes.html", {
        'heroes' : heroe
    })    

def guardar1(request):
    nombre = request.POST["nombre"]
    autor = request.POST["autor"]
    imagen = request.POST["imagen"]
    historia = request.POST["historia"]
    p = Heroe(nombre=nombre, autor=autor, imagen=imagen, historia=historia)
    p.save()
    messages.success(request, 'Heroe agregado')
    return redirect('consultar1')

def eliminar1(request, id):
    heroe = Heroe.objects.filter(pk=id)
    heroe.delete()
    messages.success(request, 'Heroe eliminado')
    return redirect('consultar1')

def detalle1(request, id):
    heroe = Heroe.objects.get(pk=id)
    return render(request, "heroeEditar.html",{
        'heroe' : heroe
    })    

def editar1(request):
    nombre = request.POST["nombre"]
    autor = request.POST["autor"]
    imagen = request.POST["imagen"]
    historia = request.POST["historia"]
    id = request.POST["id"]
    Heroe.objects.filter(pk=id).update(id=id,nombre=nombre,autor=autor, imagen=imagen, historia=historia) 
    messages.success(request, 'Heroe actualizado')
    return redirect('consultar1')

class BuscarHeroe(ListView):
    model = Heroe
    template_name = 'heroe_list.html'
    context_object_name = "heroes"

    def get_queryset(self):
        f = BuscarHeroeForm(self.request.GET or None)
        if f.is_valid():
            return Heroe.objects.filter(nombre__icontains=f.cleaned_data["heroe_nombre"]).all()
        return Heroe.objects.none()



def consultar2(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {
        'usuarios' : usuarios
    })    

def guardar2(request):
    alias = request.POST["alias"]
    personaje_fav = request.POST["personaje_fav"]
    telefono = request.POST["telefono"]
    codigo = request.POST["codigo"]
    p = Usuario(alias=alias, personaje_fav=personaje_fav, telefono=telefono, codigo=codigo)
    p.save()
    messages.success(request, 'Usuario registrado')
    return redirect('consultar2')

def eliminar2(request, id):
    usuario = Usuario.objects.filter(pk=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado')
    return redirect('consultar2')

def detalle2(request, id):
    usuario = Usuario.objects.get(pk=id)
    return render(request, "usuarioEditar.html",{
        'usuario' : usuario
    })    

def editar2(request):
    alias = request.POST["alias"]
    personaje_fav = request.POST["personaje_fav"]
    telefono = request.POST["telefono"]
    codigo = request.POST["codigo"]
    id = request.POST["id"]
    Usuario.objects.filter(pk=id).update(id=id,alias=alias,personaje_fav=personaje_fav,telefono=telefono,codigo=codigo) 
    messages.success(request, 'Usuario actualizado')
    return redirect('consultar2')

class BuscarUsuario(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = "usuarios"

    def get_queryset(self):
        f = BuscarUsuarioForm(self.request.GET)
        if f.is_valid():
            return Usuario.objects.filter(alias__icontains=f.data["usuario_alias"]).all()
        return Usuario.objects.none()