#importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import json

#leitura da planilha de dados
dados = pd.read_csv('houses_to_rent_v2.csv')

class Apartamentos():
 
 #funcao para exibir a quantidade de apartamentos disponíveis para se alugar em uma cidade X
 def quantidade_apartamentos(cidade):
    contagem =  dados[dados['Cidade'] == cidade].shape[0]#realiza uma contagem a partir da linha 0 quando o filtro é aplicado
    print("A cidade de " + str(cidade) +" possui um total de "+ str(contagem) + " apartamentos disponíveis para se alugar!")

 #função para selecionar os y(quantidade) melhores preços da cidade X 
 def melhores_precos(cidade, qtd):
    filtro = dados[dados['Cidade'] == cidade]#filtra a cidade passada em parametro
    #transforma a cidade do objeto de filtradas em um dicionario e posteriormente salva em um arquivo json
    resultado = filtro.sort_values(by='total').head(qtd).to_dict(orient='records')#aplica outro filtro passando o valor(qtd)
    nome_arquivo = "resultados.json"
    # Abrir o arquivo no modo de escrita e salvar o JSON nele
    with open(nome_arquivo, "w") as arquivo:
        json.dump(resultado, arquivo ,indent=2, ensure_ascii=False)   
        
    print(f"{qtd} melhores preços em {cidade} foram salvos em {nome_arquivo}")
    
 #função para mostrar porcentagem de apartamentos existentes em cada cidade
 def grafico_apartamentos_por_cidade():
    cidades = dados["Cidade"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(cidades, labels=cidades.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de Categorias")
    # Exiba o gráfico
    plt.show()



