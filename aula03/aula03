# Importa a biblioteca BeautifulSoup para fazer web scraping em HTML e XML de forma eficaz
from bs4 import BeautifulSoup

# Importa a biblioteca requests para enviar solicitações HTTP e receber respostas
import requests

# Listas para armazenar informações extraídas
titulo_lista = []
link_lista = []
data_lista = []
horario_lista = []
numero_da_nota_lista = []
categoria_lista = []

# Função para acessar uma página web e retornar o HTML e o código de status HTTP
def acessar_pagina(url):
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'html.parser')
    http_code = html.status_code
    return bs, http_code

# Função para extrair informações de uma página
def extrair_info_pagina(tag_article):
    # Extrai o texto dentro da tag <h2> e remove espaços em branco extras
    titulo = tag_article.h2.text.strip()
    # Adiciona o título extraído à lista de títulos (titulo_lista)
    titulo_lista.append(titulo)
    
    # Extrai o atributo 'href' da tag <a> dentro da tag <h2>, remove espaços em branco extras e adiciona à lista de links (link_lista)
    link = tag_article.h2.a['href'].strip()
    link_lista.append(link)

    # Extrai a data do elemento que contém a classe 'icon-day', remove espaços em branco extras e adiciona à lista de datas (data_lista)
    data = tag_article.find('i', class_='icon-day').parent.text.strip()
    data_lista.append(data)

    # Extrai o horário do elemento que contém a classe 'icon-hour', remove espaços em branco extras e adiciona à lista de horários (horario_lista)
    horario = tag_article.find('i', class_='icon-hour').parent.text.strip()
    horario_lista.append(horario)

    # Extrai o número da nota do elemento que contém a classe 'subtitle', realiza algumas operações para limpar o texto e adiciona à lista de números de nota (numero_da_nota_lista)
    numero_da_nota = tag_article.find('span', class_='subtitle').text.strip().lower().replace('nota à imprensa', '').replace('n°', '').replace('nº', '').strip()
    numero_da_nota_lista.append(numero_da_nota)

    # Acessa a página usando o link obtido anteriormente e armazena o conteúdo retornado
    artigo = acessar_pagina(link)

    # Encontra o elemento que contém as categorias usando a classe 'contenttree-widget relationchoice-field', extrai o texto e adiciona à lista de categorias (categoria_lista)
    categorias = artigo[0].find('div', class_='contenttree-widget relationchoice-field').text
    categoria_lista.append(categorias)

    # Impressão das informações para verificação
    print('Título:', titulo)
    print('Link:', link)
    print('Data:', data)
    print('Horário:', horario)
    print('Número da Nota:', numero_da_nota)
    print('Categoria:', categorias)
    print('-' * 100)

# URL da página de onde as informações serão extraídas
def extrair_infos():
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa?b_start:int=30"
    bs = acessar_pagina(url)[0]
    lista_tag_article = bs.find('div', attrs={'id': 'content-core'}).find_all('article', attrs={'class': 'tileItem visualIEFloatFix tile-collective-nitf-content'})
    for tag_article in lista_tag_article:
        extrair_info_pagina(tag_article)

def main():
    extrair_infos()

if __name__ == '__main__':
    main()
