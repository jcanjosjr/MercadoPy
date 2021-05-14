from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=-'*15)
    print('-=-=-=-= Bem-vindo(a) -=-=-=-=')
    print('=-'*15)
    print('-=-=-=-= PythonShope -=-=-=-=-')
    print('=-'*15)

    print('  Selecione uma opção abaixo: ')
    print('[1] - Cadastrar produto!')
    print('[2] - Listar produto!')
    print('[3] - Comprar produto!')
    print('[4] - Visualizar Carrinho!')
    print('[5] - Fechar Pedido!')
    print('[6] - Sair do programa!')
    opcao: int = int(input('Informe a opção que deseja: '))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        lista_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Obrigado pela visita!')
        sleep(2)
        print('Volte sempre...')
        exit(0)
    else:
        print('Opção Inválida!')
        menu()


def cadastrar_produto() -> None:
    print('=-'*15)
    print('-=- Cadastro de Produto! =-=')
    print('=-'*15)
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))
    produto: Produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso.')
    sleep(2)
    menu()


def lista_produto() -> None:
    if len(produtos) > 0:
        print('=-' * 15)
        print('-=-=-=-= Vamos às compras: -=-=-=-=')
        print('=-' * 15)
        for produto in produtos:
            print(produto)
            print('=-' * 15)
            sleep(0.5)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('=-' * 15)
        print('Informe o código do produto que deseja comprar!')
        print('-='*15)
        for produto in produtos:
            print(produto)
            print('-='*15)
            sleep(0.5)
        codigo : int = int(input())
        produto = Produto = pega_produto_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(0.5)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi localizado.')
    else:
        print('Ainda não possuímos produtos no estoque.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos em carrinho!')
        for items in carrinho:
            for dados in items.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-='*15)
                sleep(2)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos do Carrinho!')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-='*15)
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        print('=-'*15)
        carrinho.clear()
        sleep(2)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()

def pega_produto_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
