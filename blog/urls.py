from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('projeto', views.projeto, name='Projetos'),
    path('post/<int:pk>/',views.post_detail, name = 'post_detail'),
]



