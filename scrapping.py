from bs4 import BeautifulSoup
import requests


def obter_pagina(url):
    try:
        page = requests.get(url)
        return page.content
    except Exception as err:
        print(f'Erro ao baixar conteúdo da url: {url}')
        print(err)

def encontrar_todos_por_classe(html, classe):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        elementos = soup.find_all( attrs={'class':classe})
        return elementos
    except Exception as err:
        print('Error ao encontrar todos por classe')
        print(f'Classe: {classe}')
        print(err)

def encontrar_um_por_classe(html, classe):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        elemento = soup.find( attrs={'class':classe})
        return elemento
    except Exception as err:
        print('Error ao encontrar todos por classe')
        print(f'Classe: {classe}')
        print(err)

def encontrar_todos_elementos(html, el):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        elementos = soup.find_all(el)
        return elementos
    except Exception as err:
        print('Error ao encontrar todos por elemento')
        print(f'Elemento: {el}')
        print(err)

def encontrar_por_texto(html, el, texto):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        cidade = soup.find(el, text=texto)
        ul = cidade.next_sibling
        return ul            
    except Exception as err:
        print(err)

def obter_texto(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup.text
    except Exception as err:
        print(err)

def obter_elemento_atributo(html, el, attr):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        elemento = soup.find(el)
        if elemento != None:
            return elemento.attrs.get(attr)
    except Exception as err:
            print('Erro ao obtert atributo do elemento')
            print(f'Elemento: {el} \nAtributo: {attr}')
# Obter todas as principais cidades através da página inicial e salvar no banco de dados.

# Ter as cidades salvas no banco de dados
# Buscar eventos por cada uma das cidades em cada uma das categorias
# Salvar os dados dos eventos

#Dados
## Data
## Hora
## Local
