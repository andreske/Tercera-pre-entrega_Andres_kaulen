from django import forms


class UsuarioForm(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField()





