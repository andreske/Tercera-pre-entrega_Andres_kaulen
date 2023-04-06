from django.shortcuts import render, get_object_or_404
from .models import Post, Comentario
from AppLugares.forms import ComentarioForm


def render_posts(request):
    posts = Post.objects.all()

    return render(request, "AppLugares/posts.html", {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        mi_formulario = ComentarioForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            comentario_save = Comentario(
                autor=informacion['autor'],
                comentario=informacion['comentario'],
                post_id=post_id
            )

            comentario_save.save()

    all_comentarios = Comentario.objects.filter(post_id__icontains=post_id)
    context = {
        "form": ComentarioForm(),
        "post": post,
        "comentarios": all_comentarios
    }
    return render(request, 'AppLugares/post_detail.html', context=context)
