# Mensagem de boas-vindas
print("Bem-vindo à Loja de Açaí e Cupuaçu do Leonardo Cardoso")

# Definição dos preços
precos = {
    'cp': {'p': 9, 'm': 14, 'g': 18},
    'ac': {'p': 11, 'm': 16, 'g': 20}
}

# Inicialização do acumulador para somar os valores dos pedidos
total_pedido = 0

# Cardápio
print("--------------------Cardápio----------------------")
print("--------------------------------------------------")
print("---|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)  |---")
print("---|     P     |    R$  9.00    |  R$ 11.00   |---")
print("---|     M     |    R$ 14.00    |  R$ 16.00   |---")
print("---|     G     |    R$ 18.00    |  R$ 20.00   |---")

# Loop principal do programa
while True:
    # Input do sabor
    sabor = input("\nDigite o código do sabor desejado (CP ou AC): ").lower()

    # Verifica se o sabor é válido
    if sabor not in precos:
        print("Sabor inválido. Tente novamente.")
        continue

    # Input do tamanho
    tamanho = input("Digite o código do tamanho desejado (P, M ou G): ").lower()

    # Verifica se o tamanho é válido
    if tamanho not in precos[sabor]:
        print("Tamanho inválido. Tente novamente.")
        continue

    # Adiciona o valor do pedido ao total
    total_pedido += precos[sabor][tamanho]

    # Pergunta se o usuário deseja pedir mais alguma coisa
    continuar = input("\nDeseja pedir mais alguma coisa? (sim/não): ").lower()

    # Se a resposta for "não" ou "n", encerra o loop
    if continuar in ['n', 'nao', 'não']:
        break

# Escreve na tela o valor total do pedido
print("\nValor total a ser pago: R$ {:.2f}".format(total_pedido))
