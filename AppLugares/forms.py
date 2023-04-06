from django import forms


class ComentarioForm(forms.Form):

    autor = forms.CharField(max_length=30)
    comentario = forms.CharField(max_length=200)

