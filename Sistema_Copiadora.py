# Mensagem de boas-vindas
print("Bem-vindo à Copiadora do Leonardo Cardoso")

# Função para escolher o serviço desejado
def escolha_servico():
    while True:
        servico = input("\nEntre com o tipo de serviço desejado:\nDIG - Digitalização\nICO - Impressão Colorida\nIPB - Impressão Preto e Branco\nFOT - Fotocópia\n").lower()
        if servico in ['dig', 'ico', 'ipb', 'fot']:
            return servico
        else:
            print("Opção inválida. Tente novamente.")

# Função para solicitar o número de páginas
def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas: "))
            if num_paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
            else:
                if num_paginas < 20:
                    return num_paginas
                elif num_paginas < 200:
                    return int(num_paginas * 0.85)
                elif num_paginas < 2000:
                    return int(num_paginas * 0.8)
                else:
                    return int(num_paginas * 0.75)
        except ValueError:
            print("Valor inválido. Tente novamente.")

# Função para escolher o serviço adicional
def servico_extra():
    while True:
        servico_adicional = input("\nDeseja adicionar algum serviço?\n1 - Encadernação simples\n2 - Encadernação de capa dura\n0 - Não querer mais nada\n")
        if servico_adicional in ['1', '2', '0']:
            return int(servico_adicional)
        else:
            print("Opção inválida. Tente novamente.")

# Chamadas das funções para obter os valores
servico = escolha_servico()
num_paginas = num_pagina()
servico_adicional = servico_extra()

# Definição dos preços
precos = {
    'dig': 1.10,
    'ico': 1,
    'ipb': 0.40,
    'fot': 0.20
}

# Adicionais de encadernação
adicional_encadernacao = {
    1: 15,
    2: 40,
    0: 0
}

# Cálculo do valor total
subtotal_servico = precos[servico] * num_paginas
total_extra = adicional_encadernacao[servico_adicional]
total = subtotal_servico + total_extra

# Escreve na tela o valor total a ser pago
print("\nValor total a ser pago: R$ {:.2f}".format(total) + " (Servico: {:.2f} * Páginas: {} + Extra: {:.2f})".format(precos[servico], num_paginas, total_extra))
