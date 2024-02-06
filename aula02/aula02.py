import requests
from bs4 import BeautifulSoup
import pandas as pd

def acessar_pagina(link):
    """
    Função responsável por acessar as páginas web.

    Parâmetros:
    - link: URL da página a ser acessada.

    Retorna:
    - bs: Objeto BeautifulSoup contendo o conteúdo HTML da página.
    """
    # Faz a requisição para a página
    pagina = requests.get(link)
    
    # Cria um objeto BeautifulSoup para análise do conteúdo HTML
    bs = BeautifulSoup(pagina.text, 'html.parser')
    
    return bs

def extrair_infos():
    # URL da página que contém as notas à imprensa
    link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa"
    
    # Acessa a página e obtém o conteúdo HTML
    pagina = acessar_pagina(link)
    
    # Encontra a seção principal onde estão as notas à imprensa (pode variar dependendo da estrutura HTML)
    notas_imprensa = pagina.find("div", attrs={"id":"content-core"}).find_all("article")
    
    # Itera sobre cada artigo/nota à imprensa
    for nota_imprensa in notas_imprensa:
        # Obtém o título da nota à imprensa
        titulo = nota_imprensa.find('h2').text.strip()
        
        # Imprime o título da nota à imprensa
        print(titulo)
        
        # Adiciona uma separação para melhor visualização
        print("#"*100)

def main():
    # Chama a função para extrair informações
    extrair_infos()

if __name__ == "__main__":
    # Chama a função principal se o script for executado diretamente
    main()
