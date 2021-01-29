import requests

def main():

    print('================')
    print('===== CEP ======')
    print('================')
    print()

    #solicitar o cep
    cep = (input("Digite o CEP a ser consultado:\t"))
    cep = cep.strip()
    #validar o tamanho
    if len(cep) != 8:
        print(f"o CEP deve ter 8 digitos e voce digitou {len(cep)}")
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    dados_endereco = request.json()

    if 'erro' not in dados_endereco:
        print('\n\n===CEP encontrado===\n\n\n')

        print(f"CEP: {dados_endereco['cep']}")
        print(f"LOG: {dados_endereco['logradouro']}")
        print(f"COMP: {dados_endereco['complemento']}")
        print(f"BAIRRO: {dados_endereco['bairro']}")
        print(f"LOC: {dados_endereco['localidade']}")
        print(f"ESTADO: {dados_endereco['uf']}")

    else:
        print(f'{cep}: CEP invalido')
    
    opcao = int(input("\n\n\nDeseja fazer uma nova consulta? \n 1-Sim \n 2-Não \n 3-Sair \n"))
    if opcao == 1:
        main()
    elif opcao ==2:
        exit()
    else:
        print("Tem Certeza?, Responda novamente!!")
        main()

if __name__== '__main__':
    main()
