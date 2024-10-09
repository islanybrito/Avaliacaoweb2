from django import forms
from .models import Cliente
from .models import Pedido
from .models import Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']
        

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descricao', 'valor', 'cliente']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'quantidade', 'pedido']