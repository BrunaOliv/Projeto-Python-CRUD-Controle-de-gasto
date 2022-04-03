from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao= models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'

    def __str__(self):
        return self.descricao
        
    def valor_total(self):
        transacoes = self.valor.all() # aplicar filtros padroes se precisar
        preco_total = 0.00
        for transacao in transacoes:
            preco_total += transacao.preco
            print(preco_total)
            return preco_total