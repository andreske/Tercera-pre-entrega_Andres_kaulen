from django.urls import path

from AppLugares.views import render_posts, post_detail

app_name = "AppLugares"

urlpatterns = [
    path('', render_posts, name='post'),
    path('<int:post_id>', post_detail, name="post_detail")
]



