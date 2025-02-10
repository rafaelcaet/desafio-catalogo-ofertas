from django.urls import path
from .views import listar_produtos,listar_produtos_template

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
]
urlpatterns += [
    path('produtos/lista/', listar_produtos_template, name='listar_produtos_template'),
]