from Apartamentos import Apartamentos
from ConexaoBD import ConexaoBancoDeDados

#instanciando/criando objeto
ap = Apartamentos #objeto de apartamentos

#instância da classe ConexaoBancoDeDados
conexao = ConexaoBancoDeDados()



permanece = True

while(permanece == True):
    print("Bem vindo ao menu")
    print("1- Filtrar uma cidade Especifica ")
    print("2- Exibir Gráfico")
    print("3- Incluir novo apartamento")
    print("4- Sair")
    
    op = input("Entre com a opção Desejada: ")
    if (op == '1'):
        #entrada de dados
        busca_cidade = input("Escolha qual cidade você deseja filtrar: ")
        leque_opcoes = int(input("Informe a quantidade mínima de casas nos melhores preços que você deseja consultar: "))

        #chamando métodos da classe apartamento
        ap.quantidade_apartamentos(busca_cidade)#retorna quantidade de apartamentos em cada cidade
        ap.melhores_precos(busca_cidade,leque_opcoes)# lista x casas mais baratas de todas as opçoes
    elif (op == '2'):
        ap.grafico_apartamentos_por_cidade()#retorna um grafico pizza com as porcentagens
    elif(op == '3'):
        apartamento_id = int(input("Informe o id do apartamento: "))
        cidade_apartamento = input("Informe a cidade em que o apartamento está localizado: ")
        metros_quadrados = int(input("Informe os metros² do apartamento: "))
        numero_quarto = int(input("Informe a quantidade de quarto(s): "))
        numero_banheiro = int(input("Informe a quantidade de banheiro(s): "))
        vagas_estacionamento = int(input("Informe a quantidade de vaga(s) no estacionamento: "))
        aceita_animais = input("Aceita animais? Entre com 'Aceita' ou 'Nao Aceita': ")
        valor_aluguel = float(input("Informe o valor do aluguel: "))
        valor_iptu = float(input("Informe o valor do IPTU: "))
        valor_seguranca = float(input("Informe o valor do Segurança: "))

        conexao.insert_banco(apartamento_id,cidade_apartamento,metros_quadrados,numero_quarto,numero_banheiro,vagas_estacionamento,aceita_animais,valor_aluguel,valor_iptu,valor_seguranca)
    elif(op == '4'):
        print("Saindo")    
        permanece = False
    elif(op != '1' and op != '2' and op != '3' and op != '4'):
        print("Opção Inválida")    