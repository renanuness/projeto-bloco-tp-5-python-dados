from  scrapping import *
import database as db
import re
import sys
from evento_ambiente import definir_tipo_ambiente
options = (sys.argv)

if '-d' in options:
    db.destruir_db()
    if '-o' in options:
        exit()

db.criar_estrutura()

pensa_no_evento_url = 'https://www.pensanoevento.com.br'

# Ler eventos de 16/03 até 30/04
def percorrer_agenda_marco_abril():
    mes = 3
    dia = 16
    while(True):
        print(f'Obtendo dados do dia {dia} do mês {mes}')
        url = f'{pensa_no_evento_url}/agenda?dia={"{:02d}".format(dia)}&mes={"{:02d}".format(mes)}&ano={2025}'
        extrair_eventos(url)
        print(f'Extração de evento concluída')
        dia += 1
        if mes == 3 and dia > 31:
            dia = 1
            mes = 4

        if mes == 4 and dia > 30:
            break

def extrair_eventos(agenda_url):
    agenda_page = requests.get(agenda_url)

    divs_eventos = encontrar_todos_por_classe(agenda_page.content, 'grid_2')
    print(f'{len(divs_eventos)} encontrados...')
    for evento in divs_eventos: 
        a = obter_elemento(str(evento), 'a')
        link = obter_elemento_atributo(str(a), 'a', 'href')
        print(f'Extraindo informação do link: {link}')
        processar_dados_evento(link)
        
def processar_dados_evento(link: str):
    pagina_evento = requests.get(link)
    if not pagina_evento.ok:
        return
    
    info_lista = encontrar_um_por_classe(pagina_evento.content, 'list')
    info_itens = encontrar_todos_elementos(str(info_lista), 'li')
        
    metadados = []
    site_id = link.split('/')[4]
    nome = ''
    data = ''
    hora_inicio = ''
    hora_fim = ''
    classificacao = ''
    local = ''
    instagram = ''
    dados_eventos = obter_elemento(pagina_evento.content, 'main')
    tipo_ambiente = definir_tipo_ambiente(str(dados_eventos))

    metadados.append({'descricao':'tipo_ambiente', 'valor': tipo_ambiente})
    for item in info_itens:
        texto = obter_texto(str(item)).strip()

        nome_match = re.search(r'^Nome do Evento:\s*(.*)', texto)
        data_match = re.search(r'^Data:\s*(\d{2}\/\d{2}\/\d{4})', texto)
        hora_inicio_match = re.search(r'^Horário de Abertura:\s*(.*)', texto)
        hora_fim_match = re.search(r'^Horário de término:\s*(.*)', texto)
        classificacao_match = re.search(r'Classificação:\s*(.*)', texto)
        local_match = re.search(r'Local:\s*(.*)', texto)
        instagram_match = re.search(r'Instagram:\s*(.*)', texto)

        if nome_match:
            nome = nome_match[1]

        if data_match:
            data = data_match[1]
            metadados.append({ 'descricao': 'data', 'valor': data})

        if hora_inicio_match:
            hora_inicio = hora_inicio_match[1]
            metadados.append({ 'descricao': 'hora_inicio', 'valor': hora_inicio})

        if hora_fim_match:
            hora_fim = hora_fim_match[1]
            metadados.append({ 'descricao': 'hora_fim', 'valor': hora_fim})

        if classificacao_match:
            classificacao = classificacao_match[1]
            metadados.append({ 'descricao': 'classificacao', 'valor': classificacao})

        if local_match:
            local = local_match[1]
            metadados.append({ 'descricao': 'local', 'valor': local})

        if instagram_match:
            instagram = instagram_match[1]
            metadados.append({ 'descricao': 'instagram', 'valor': instagram})
    
    #salvar evento e obter o id
    cidade_id = processar_cidade(pagina_evento.content)
    evento_id =  inserir_obter_evento_id(nome, site_id, cidade_id)
    #obter categorias
    processar_categorias(pagina_evento.content, evento_id)

    processar_metadados(evento_id, metadados)
   
def processar_cidade(content):
    try:
        cards = encontrar_todos_por_classe(content, 'card-text')
        cidade = None
        estado = None
        for card in cards:
            texto = obter_texto(str(card))
            cidade_match = re.search(r'([A-zÀ-ú\s])*(\/){1}([A-Z]{2})', texto)
            if cidade_match != None:
                cidade_estado = cidade_match.group(0).split('/')
                cidade = (str(cidade_estado[0])).strip()
                estado = cidade_estado[1]

        if cidade == None or estado == None:
            # 1 será o valor default para eventos sem cidade
            return 1

        cidade_existente = db.obter_cidade_estado(cidade, estado)
        if cidade_existente == None:
            db.inserir_cidade(cidade, estado)
            cidade_existente = db.obter_cidade_estado(cidade, estado)

        return cidade_existente[0]
    except Exception as err:
        print('Erro ao processar cidade')
        print(err)
            
def inserir_obter_evento_id(nome, site_id, cidade_id):
    try:
        evento_existente = db.obter_evento_por_site_id(site_id)
        if evento_existente == None:
            db.inserir_evento(nome, cidade_id, site_id)
            evento_existente = db.obter_evento_por_site_id(site_id)
        
        return evento_existente[0]
    except Exception as err:
        print('Erro ao inserir evento')
        print(f'Evento: {nome}')
        print(err)

def processar_categorias(content, evento_id):
    categorias = encontrar_todos_por_classe(content, 'text-muted badge badge-outline small')
    for categoria_el in categorias:
        categoria_nome = obter_texto(str(categoria_el))
        categoria = adicionar_obter_categoria(categoria_nome)
        db.inserir_evento_categoria(evento_id, categoria[0])

def adicionar_obter_categoria(nome):
    categoria_existente = db.obter_categoria_por_nome(nome)
    if categoria_existente == None:
        db.inserir_categoria(nome)
        categoria_existente = db.obter_categoria_por_nome(nome)

    return categoria_existente

def processar_metadados(evento_id, metadados):
    for metadado in metadados:
        tipo_metadado_id = obter_adicionar_tipo_metadado(metadado['descricao'])
        db.inserir_evento_metadados(evento_id, tipo_metadado_id, metadado['valor'])

def obter_adicionar_tipo_metadado(descricao):
    descricao_existente = db.obter_tipo_metadado_por_descricao(descricao)

    if descricao_existente == None:
        db.inserir_tipo_metadados(descricao)
        descricao_existente = db.obter_tipo_metadado_por_descricao(descricao)

    return descricao_existente[0]

if '-c' in options:
    percorrer_agenda_marco_abril()

if '-um' in options:
    db.mostrar_todos()

if '-dois' in options:
    db.mostrar_proximos()

if '-tres' in options:
    db.mostrar_por_cidade('Florianópolis')

if '-quatro' in options:
    db.mostrar_eventos_ceu_aberto()

if '-cinco' in options:
    db.mostrar_todos_metadados()