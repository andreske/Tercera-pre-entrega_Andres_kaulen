from django.shortcuts import render
from AppWeb.models import Usuario, Direccion, Solicitud
from AppWeb.forms import UsuarioForm, DireccionForm, SolicitudForm, BusquedaUsuarioForm


def home(request):
    return render(request, "index.html")


def usuarios(request):
    if request.method == "POST":
        mi_formulario = UsuarioForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario_save = Usuario(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email']
            )
            usuario_save.save()

    all_usuarios = Usuario.objects.all()
    context = {
        "usuarios": all_usuarios,
        "form": UsuarioForm(),
        "form_busqueda": BusquedaUsuarioForm(),
    }
    return render(request, "AppWeb/usuarios.html", context=context)


def busqueda_usuario(request):
    mi_formulario = BusquedaUsuarioForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        usuarios_filtrados = Usuario.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "usuarios": usuarios_filtrados
        }

        return render(request, "AppWeb/busqueda_usuario.html", context=context)


def direcciones(request):
    if request.method == "POST":
        mi_formulario = DireccionForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            direccion_save = Direccion(
                calle=informacion['calle'],
                numero=informacion['numero'],
                ciudad=informacion['ciudad']
            )
            direccion_save.save()

    all_direcciones = Direccion.objects.all()
    context = {
        "direcciones": all_direcciones,
        "form": DireccionForm()
    }
    return render(request, "AppWeb/direcciones.html", context=context)


def solicitudes(request):
    if request.method == "POST":
        mi_formulario = SolicitudForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            solicitud_save = Solicitud(
                nombre_solicitud=informacion['nombre_solicitud'],
                cantidad=informacion['cantidad']
            )
            solicitud_save.save()

    all_solicitudes = Solicitud.objects.all()
    context = {
        "solicitudes": all_solicitudes,
        "form": SolicitudForm()
    }
    return render(request, "AppWeb/solicitudes.html", context=context)
