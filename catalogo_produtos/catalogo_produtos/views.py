from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from .models import Produto
from .scraper import coletar_produtos

def listar_produtos(request):
    produtos = Produto.objects.all()
    filtro_frete_gratis = request.GET.get('frete_gratis')
    filtro_full = request.GET.get('full')

    if filtro_frete_gratis:
        produtos = produtos.filter(frete_gratis=True)
    if filtro_full:
        produtos = produtos.filter(tipo_entrega='full')
    coletar_produtos()
    paginator = Paginator(produtos, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    produtos_json = list(page_obj.object_list.values())
    return JsonResponse({"produtos": produtos_json, "page": page_obj.number, "num_pages": paginator.num_pages}, safe=False)

def listar_produtos_template(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})
