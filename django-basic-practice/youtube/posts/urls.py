from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', view=views.post_list, name='post_list'),
    path('post_detail/<int:post_id>', view=views.post_deatil, name='post_detail'),
    path('post_form/', view=views.post_create, name='post_create'),
]