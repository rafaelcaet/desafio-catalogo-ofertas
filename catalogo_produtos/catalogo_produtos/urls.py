from django.urls import path
from .views import list_products,list_products_template

urlpatterns = [
    path('produtos/', list_products, name='listar_produtos'),
]
urlpatterns += [
    path('produtos/lista/', list_products_template, name='listar_produtos_template'),
]