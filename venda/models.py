from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome+" - "+self.cpf
    
class Pedido(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao+" - "+str(self.valor)

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao+" - "+str(self.valor)
