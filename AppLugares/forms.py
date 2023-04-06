from django import forms


class UsuarioForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class ComentarioForm(forms.Form):

    autor = forms.CharField(max_length=30)
    comentario = forms.CharField(max_length=200)

