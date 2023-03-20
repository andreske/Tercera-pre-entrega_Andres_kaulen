from django import forms


class UsuarioForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField()


class BusquedaUsuarioForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)


class DireccionForm(forms.Form):

    calle = forms.CharField(max_length=30)
    numero = forms.IntegerField()
    ciudad = forms.CharField(max_length=30)


class SolicitudForm(forms.Form):

    nombre_solicitud = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()


