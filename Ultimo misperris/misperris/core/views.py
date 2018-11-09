from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Mascota,Raza,Genero,Estado
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'core/home.html')

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def menu(request):
    return render(request, 'core/menu.html')

#AGREGAR OK
def agregar_mascotas(request):

    razas = Raza.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    variables = {
        'razas':razas,
        'generos':generos,
        'estados':estados
    }

    if request.POST:
        perro = Mascota()
        perro.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        perro.genero = genero
        perro.imagen = request.POST.get('file_foto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        perro.estado = estado

        try:
            perro.save()
            variables['mensaje'] = 'Mascota Guardada Correctamente'
        except:
            variables['mensaje'] = 'ERROR! No se ha podido guardar'

    return render(request, 'core/agregar_mascota.html', variables)
########################################################################

#@login_required
def agregar_mascota(request):

    perri = Raza.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    variables = {
        'perri':perri,
        'estado':estado,
        'raza':raza,
    }

    if request.POST:
        perro = Mascota()
        perro.nombre = request.POST.get('txtNombre')

        razita = Raza()
        razita.id = request.POST.get('cboRaza')
        perro.raza = razita

        perro.imagen = request.POST.get('txtFoto')

        estadito = Estado()
        estadito.id = request.POST.get('cboEstado')
        perro.estado = estadito

        perro.razita = Mascota
        perro.estadito = Mascota
        perro.save()

        try:
            variables['mensaje'] = 'Mascota Guardada Exitosamente'
        except:
            variables['mensaje'] = 'ERROR! No se ha podido guardar Mascota'

    return render(request,'core/agregar_mascota.html',variables)


#LISTAR OK
def listar_mascotas(request):

    mascotas = Mascota.objects.all()

    return render(request,'core/listar_mascotas.html',{
        'mascotas':mascotas
    })
#############################################################

#ELIMINAR OK
def eliminar_mascotas(request, id):

    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Mascota Eliminada Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar Mascota"
        messages.error(request, mensaje)
    
    return redirect('listar_mascotas')
#######################################################



def modificar_mascota(request, id):

    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    variables = {
        'mascota':mascota,
        'razas':razas,
        'generos':generos,
        'estados':estados
    }

    if request.POST:
        perro = Mascota()
        perro.id = request.POST.get('txtId')
        perro.nombre = request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        perro.raza = raza
        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        perro.genero = genero
        perro.imagen = request.POST.get('file_foto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        perro.estado = estado

        try:
            perro.save()
            messages.success(request, 'Mascota Modificada Exitosamente')
        except:
            messages.error(request, 'ERROR! No se ha podido modificar')
        return redirect('listar_mascotas')


    return render(request,'core/modificar_mascota.html', variables)


















