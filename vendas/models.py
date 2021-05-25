from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Sum, F, FloatField, Max, DecimalField
from clientes.models import Person
from produtos.models import Produto
from .managers import VendaManager
# Create your models here.


class Vendas(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    impostos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    # produtos = models.ManyToManyField(Produto, blank=True)
    nfe_emitida = models.BooleanField(default=False)

    objects = VendaManager()

    class Meta:
        # cria permissoes personalizaveis
        permissions = (
            ('setar_nfe', 'Usuario pode alterar parametro NFe'),
            ('remover_nfe', 'Usuario pode alterar para Nfe nao emitida'),
            ('ver_dashboard', 'Pode vizualizar dashboard')
        )

    def calcular_total(self):
        tot = self.itemdopedido_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0
        print(tot)
        tot = tot - float(self.desconto) - float(self.impostos)
        print(tot)
        self.valor = float(tot)
        self.save()
        # Vendas.objects.filter(id=self.id).update(valor=float(tot))

    def __str__(self):
        return self.numero


class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.produto.descricao


@receiver(post_save, sender=ItemDoPedido)
def update_vendas_total(sender, instance, **kwargs):
    instance.venda.calcular_total()


# @receiver(post_save, sender=Vendas)
# def update_vendas_total2(sender, instance, **kwargs):
#     instance.calcular_total()
