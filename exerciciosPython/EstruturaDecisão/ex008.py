# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

primeiroProdutoMsg = 'Digite o preço do primeiro produto R$: '
segundoProdutoMsg = 'Digite o preço do segundo produto R$: '
terceiroProdutoMsg = 'Digite o preço do terceiro produto R$: '

primeiroProduto = float(input(primeiroProdutoMsg))
segundoProduto = float(input(segundoProdutoMsg))
terceiroProduto = float(input(terceiroProdutoMsg))

primeiroItem = 'Primeiro item '
segundoItem = 'Segundo item '
terceiroItem = 'Terceiro item '

analise = 'De acordo com análise feita com base nos preços dos três produtos.'
menorPreco = f'O produto com menor preço é o de valor R$: '

produtoMaisBarato = primeiroProduto
if segundoProduto < primeiroProduto and segundoProduto < terceiroProduto:
    produtoMaisBarato = segundoProduto
if terceiroProduto < primeiroProduto and terceiroProduto < segundoProduto:
    produtoMaisBarato = terceiroProduto

print(analise)
print(menorPreco, '{:.2f}'.format(produtoMaisBarato))