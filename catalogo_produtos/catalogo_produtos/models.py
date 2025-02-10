from django.db import models
# produto
class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    imagem_produto = models.URLField()
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    preco_sem_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_desconto = models.FloatField(null=True, blank=True)
    opcao_parcelamento = models.CharField(max_length=255, null=True, blank=True)
    link_produto = models.URLField()
    tipo_entrega = models.CharField(max_length=50, choices=[('full', 'Full'), ('normal', 'Normal')])
    frete_gratis = models.BooleanField(default=False)
    data_raspagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome