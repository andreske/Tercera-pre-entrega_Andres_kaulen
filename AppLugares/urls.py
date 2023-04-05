from django.urls import path

from AppLugares.views import render_posts, post_detail

urlpatterns = [
    path('', render_posts, name='post'),
    path('<int:post_id>', post_detail)
]



