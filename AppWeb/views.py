from django.shortcuts import render
from AppWeb.models import Usuario
from AppWeb.forms import UsuarioForm, BusquedaUsuarioForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, "AppWeb/home.html")


def base(request):
    return render(request, "base.html")


def about(request):
    return render(request, "AppWeb/about.html")


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
    return render(request, "AppWeb/about.html", context=context)


def busqueda_usuario(request):
    mi_formulario = BusquedaUsuarioForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        usuarios_filtrados = Usuario.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "usuarios": usuarios_filtrados
        }

        return render(request, "AppWeb/busqueda_usuario.html", context=context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppWeb/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "AppWeb/inicio.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "AppWeb/inicio.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()

    return render(request, "AppWeb/login.html", {"form": form})

