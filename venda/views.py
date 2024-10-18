from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Pedido
from .forms import ClienteForm
from .forms import PedidoForm
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string


@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html' , {'clientes': clientes})

@login_required
def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_clientes.html', {'form':form})

@login_required
def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})

@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})


@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})

@login_required
def criar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/criar_pedido.html', {'form': form})

@login_required
def atualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/atualizar_pedido.html', {'form': form})

@login_required
def deletar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        pedido.delete()
        return redirect('listar_pedidos')  # Redireciona para a lista de pedidos
    return render(request, 'pedidos/deletar_pedido.html', {'pedido': pedido})

@login_required
def exportar_clientes_pdf(request):
    # Buscando todos os usuários
    clientes = Cliente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('clientes/clientes_pdf.html', {'clientes': clientes})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response

@login_required
def exportar_pedidos_pdf(request):
    # Buscando todos os usuários
    pedidos = Pedido.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('pedidos/pedidos_pdf.html', {'pedidos': pedidos})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response
@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/criar_produto.html', {'form': form})

@login_required
def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/atualizar_produto.html', {'form': form})

@login_required
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')  # Redireciona para a lista de pedidos
    return render(request, 'produtos/deletar_produto.html', {'produto': produto})

@login_required
def exportar_produtos_pdf(request):
    # Buscando todos os usuários
    produtos = Produto.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('produtos/produtos_pdf.html', {'produtos': produtos})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="produtos.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response