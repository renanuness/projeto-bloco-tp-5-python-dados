from  scrapping import *
from database import *
import json

sympla_url = 'https://www.sympla.com.br'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'priority': 'u=0, i',
    "accept-language": 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    "cache-control": 'max-age=0',
    'sec-ch-ua': '\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"',
    'sec-ch-ua-mobile': '?0^',
    "sec-ch-ua-platform": "\"Windows\"",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'cookie': '_gcl_au=1.1.1593472618.1741442889; _fbp=fb.2.1741442890079.904834992123270971; _tt_enable_cookie=1; _ttp=01JNV1BFJDY32EDB6XG32AS48B_.tt.2; intercom-id-j3shov1b=29d1c8a9-830b-4d84-9ec0-109704f85e09; intercom-device-id-j3shov1b=664cdb98-5891-4504-b0f3-8c6928cae494; hubspotutk=6d3fe5a57a492dd7c186c9084fb4e303; __hssrc=1; tck_id=07c30d15b2a040d8810e123bb583c104; session_id=668a9ed8c84240c0b6a06befb58eebc4; _spbidw=qmi3k; _symplaSession-prod=s%3AXI6BJqYwc5_7VDyjCiZpXEyGHfjReSRB.ChAgbtKfcjcSwgkP%2Fvslvuz6Oq1PLmP01aiVimb6aaM; sympla_tck=%7B%22id%22%3A%2267cc4f579f4ca6.11937133fae1615bbe44a1a11988599fe072f177%22%2C%22created_at%22%3A1741442903%7D; 64d86277adaf92353b7a89da3d6dc9cb=21c8d4df8d7686a702dac4976033fcdbff093fd1a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2224684359%22%3Bi%3A1%3Bs%3A29%3A%22renan.nsilva%40al.infnet.edu.br%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A1%3A%7Bs%3A13%3A%22lastLoginTime%22%3Bi%3A1741442903%3B%7D%7D; sympla_sid=67cc4f57dd678.24684359; s_buyer_status=WOQK6XTsnQ174wkplMRCm2Zwy9HvlvmTbrAR5JPd5A==; OptanonAlertBoxClosed=2025-03-08T14:14:57.887Z; s_geo_location_notification=closed; _ga_TVWXB4ZXRZ=GS1.1.1741449263.2.0.1741449263.0.0.0; __gads=ID=c5433861278860ac:T=1741450663:RT=1741451264:S=ALNI_Mb90We92jTNyuPDBmP3nnUmGhtWKw; __gpi=UID=00001067a2d73e12:T=1741450663:RT=1741451264:S=ALNI_MZDB5UhyggAljrTFIEKrcd9EZfVqg; __eoi=ID=9e80b32530c1052e:T=1741450663:RT=1741451264:S=AA-AfjaEmoLmAi4CIa9EgJ9wj4O2; _cfuvid=FDBYeVsh7V0zSq8qdJwgLzpAclJe.Zy2N2A6bcy2vDM-1741557055475-0.0.1.1-604800000; optimizelyEndUserId=oeu1741611574439r0.5081390018791798; optimizelySegments=%7B%224225866243%22%3A%22gc%22%2C%224230684143%22%3A%22false%22%2C%224232464299%22%3A%22direct%22%7D; optimizelyBuckets=%7B%7D; _gid=GA1.3.242176152.1741612580; _ga_HY91WCS3L8=GS1.1.1741612579.1.1.1741612589.50.0.2100904380; cto_bundle=JGxsH19EWnhEeHJmSFNVMktHRFdxbXElMkZFRHdwN0l2VWRPTzNKSVFGbnYlMkJXWFd2Q013TldJczd5cGlMQWtQZERMYWVnZDRLUVFhSWMxNGhMMnUyY2ZyMzBDN09SUlozMmdvSlpJR3haQUJkTmJWcGFVY2FVVjI5QmtvVHBnd24xV1UyT0V1bU5JajU5ZG1IMU10ZjB5azVQNjdPTTAlMkJKV2RhQVRkRjRodEhHZWJ0a3ZudlZHRVklMkJtaEhCSldiR2VJU05CbyUyRlZ1dkZKSkRaZ1pZS0c2M0ZLZE03Q2xvcFhrc1ZXa0xsaEFlNllTa2EybHhMdXJSY2ElMkZpT0RoYko0JTJCbkpKTjFzOHUlMkZJRm1jMXhvY3RDU2xBems5VWclM0QlM0Q; sympla=una4tnliqn9e38njthnko4jt82; dismiss-banner-privacy-policy=closed; mp_4c784276a5f0fe1e507c4fd6030030fe_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19576ce402f618-06c78909fc20cf-26011a51-1fa400-19576ce402f619%22%2C%22%24device_id%22%3A%20%2219576ce402f618-06c78909fc20cf-26011a51-1fa400-19576ce402f619%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_N4K980KPQ6=GS1.3.1741644545.2.0.1741644545.0.0.0; _hjSessionUser_1581841=eyJpZCI6ImY5OGE2YjJmLTA5MjMtNWE4OS1hN2Y5LWU4NTVhZjVkNTE0ZSIsImNyZWF0ZWQiOjE3NDE0NTQ5ODM5ODcsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1089578805.1741442890; eb37858f6fff7d7e08cd0f8ff82b704d=279e6291cb1a66f98a847cacf3073c88ff2d5d20a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2224684359%22%3Bi%3A1%3Bs%3A0%3A%22%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; _hjSessionUser_548816=eyJpZCI6IjUzMGNiYjU0LWRlMTQtNWZhNy05ZDA2LTZhNTAwZDdjYWYyOCIsImNyZWF0ZWQiOjE3NDE2NDU1MjkyNTMsImV4aXN0aW5nIjpmYWxzZX0=; AWSALB=qUktY61v/DyWHLOCpwJUP2yVSdNndt3k/F5Rtbk1mJdLpJN2GpLEqeqJTbTvc385VNKK9wjIp/phD7qcTwxIgWd+9Bte+lZwew7MzWU309tC/A84sorFHAfIWw30; AWSALBCORS=qUktY61v/DyWHLOCpwJUP2yVSdNndt3k/F5Rtbk1mJdLpJN2GpLEqeqJTbTvc385VNKK9wjIp/phD7qcTwxIgWd+9Bte+lZwew7MzWU309tC/A84sorFHAfIWw30; __hstc=43288186.6d3fe5a57a492dd7c186c9084fb4e303.1741442893219.1741644513933.1741650468744.10; s_user_location={\"city\":\"Fortaleza\",\"coordinates\":{\"lat\":-3.73765,\"lon\":-38.51538},\"sk\":952,\"slug\":\"fortaleza-ce\"}; __cf_bm=7KUCHjRlUHxeB5_tEupjOp5xuNXPISciI4zP324EEsQ-1741651491-1.0.1.1-Jc0p2CP6SL0vM4HlvQNj30iwXpRBNFdDqYNG9kLWlqGEuLivKwsQddi2_LbdENPOYNksi5.ShyhunFp4XouwU92oHuzkWjl7dRsPgUrwLB0; cf_clearance=xES.M8cUb6oUaJtQppQbx7gQFlANugsvviUPiB2UNIE-1741651491-1.2.1.1-ZsV83rvaCnG6egYKjeMpIrhWpbu_ErGZawEPGIBrV8UDKrhXPVSl3fhzpbFcGwqzlaXelx3WRkkQgbDUgaLconPV3ETyfew9jUKDcaRPo4GUisng_VVL6Knl.caG4CzytGk2RTus0QS_IPn6irAWPycHURjhZXfyooiFfol4VK.Cn9y8FAgzXXjr2fdUlcvWdgJj46Vi2b0pQPkMEHcUhJmnxWu.dpq8qqBvfApcjilROyCRKcQfQpPSV5Z8rn1D5RsJG2DGVzz.u4o3oIcZrefpp0jCFrVDQ0WMNghvPKnnP46GikBuctuku1jBMDt8zoHoL7yPYxddzsYzRN8QNWYRErK1NnSokBzwFR_CVmI; _clck=158cay8%7C2%7Cfu4%7C0%7C1893; QueueITAccepted-SDFrts345E-V3_symplavisitorpeak=EventId%3Dsymplavisitorpeak%26RedirectType%3Dsafetynet%26IssueTime%3D1741651628%26Hash%3D43f94a6fe90ec66506961e0f468f84ab66e4537c4c8bb48f8d0f41e15c78549e; _uetsid=c625b200fc2611efb8d059795bff0b25; _uetvid=29723b3026a311efbe3e1991ada9e26c; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+10+2025+21%3A07%3A08+GMT-0300+(Hor%C3%A1rio+Padr%C3%A3o+de+Bras%C3%ADlia)&version=202408.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false&geolocation=%3B; _ga_KXH10SQTZF=GS1.1.1741650467.10.1.1741651628.60.0.1288278873; _clsk=6e3vll%7C1741651629122%7C5%7C0%7Cj.clarity.ms%2Fcollect; __hssc=43288186.8.1741650468744; sympla_rv=%7B%22recents%22%3A%5B%222831890%22%2C%222830785%22%2C%222847892%22%2C%222847892%22%2C%222847892%22%2C%222777036%22%5D%2C%22history%22%3A%7B%222847892%22%3A1741650951%7D%7D; intercom-session-j3shov1b=NXlLVEhyaE5Dam0wUVBKWXRFVjZiK29yZ3Z4Q2wzL21NRlBWalVRYTkrV2R1TldVZExrclpWL2o4aUJXKzkrMG5icHBscUViQUNBeEdPeitNdm4yRjRtdjljM05YZ21nL2RjWmRvNE5XTzQ9LS1KUGZnSTBrY2NOTVY0a21pMzVzVkNRPT0=--240b582940cefd3cdc9458361b2caf938d10bd44; _dd_s=logs=1&id=d4d0f38d-aaed-46cf-b7ee-c02f0c4fa988&created=1741650407307&expire=1741652545219'
}

pagina = obter_pagina(sympla_url)

def extrair_cidades():
    cidades = encontrar_por_texto(pagina, 'h4', 'Cidades')
    cidades_str = []
    for c in cidades:
        cidade = obter_texto(str(c))
        cidade_link = obter_elemento_atributo(str(c), 'a', 'href')
        if cidade != None:
            cidades_str.append((cidade, cidade_link))

    return cidades_str

def extrair_categorias():
    categorias = encontrar_por_texto(pagina, 'h4', 'Categorias')
    categorias_str = []
    for c in categorias:
        categoria = obter_texto(str(c))
        categoria_link = obter_elemento_atributo(str(c), 'a', 'href')
        if categoria != None and categoria != 'Sympla Play':
            categorias_str.append((categoria, categoria_link))
    
    return categorias_str

cidades = extrair_cidades()
categorias = extrair_categorias()

#region Inicialização
criar_estrutura()
inserir_cidades(cidades)
inserir_categorias(categorias)
#endregion

def encontrar_eventos():
    try:
        cidades = obter_todas_cidades()
        categorias = obter_todas_categorias()

        for cidade in cidades:
            encontrar_eventos_cidade(cidade, categorias)
    except Exception as err:
        print('Erro ao encontrar eventos')
        print(err)

def encontrar_eventos_cidade(cidade, categorias):
    for categoria in categorias:
        processar_eventos_cidade(cidade, categoria)

def obter_url(cidade, categoria, pagina):
        categoria_link = categoria[2]
        categoria_link = str(categoria_link).split('/')
        pagina_atual = 1
        url = f'{sympla_url}{cidade[2]}/{categoria_link[2]}?c=em-alta&ordem=month_trending_score&ordem=start-date&page={pagina_atual}'
        return url

def processar_eventos_cidade(cidade, categoria):
    try:
        pagina_atual = 1
        while(True):
            url = obter_url(cidade, categoria, pagina_atual)
            pagina_eventos = requests.get(url)
            if not pagina_eventos.ok:
                print(f'Erro ao buscar dados da página {url}')
                continue
            eventos_cards = obter_eventos_pagina(pagina_eventos.content)
            for card in eventos_cards:
                processar_evento_card(card)
            #nome,categoria_id, cidade_id
            pagina_atual += 1
    except Exception as err:
        print('Erro ao processar eventos da cidade')
        print(f'Cidade: {cidade}')
        print(f'Categoria: {categoria}')
        print(err)

def processar_evento_card(card):
    # local_el = encontrar_um_por_classe(str(card), 'pn67h1a')
    # local = local_el.text
    # print(local)
    
    
    # nome_el = encontrar_um_por_classe(str(card), 'pn67h18')
    # nome = nome_el.text
    # print(nome)

    # data_el = encontrar_um_por_classe(str(card), 'qtfy413')
    # data = data_el.text
    # salvar_data(data)

    link = obter_elemento_atributo(str(card), 'a', 'href')
    link_partes = link.split('/')
    evento_id = link_partes[len(link_partes)-1]
    link += '?referrer=sympla.queue-it.net'
    print(link)
    pagina_evento = requests.get(link, headers=headers)
    if not pagina_evento.ok:
        print(f'Erro ao obter página do evento com link: {link}')
        return
    
    obter_evento_preco(evento_id)
    processar_pagina_evento(pagina_evento)

def processar_pagina_evento(pagina):
    print(pagina.content)

def obter_evento_preco(evento_id):
    url = f'https://event-page.svc.sympla.com.br/api/event-bff/purchase/event/{evento_id}/tickets'
    lotes_json = requests.get(url)
    if not lotes_json.ok:
        print(f'Não foi possível obter dados da página: {url}')
    
    lotes_obj = json.loads(lotes_json.text)
    for lote in lotes_obj:
        ingressos = lote['installments']
        for ingresso in ingressos:
            print(ingresso['price']['decimal'])

def obter_eventos_pagina(html):
    try:
        evento_cards = encontrar_todos_por_classe(html, 'sympla-card')
        return evento_cards
    except Exception as err:
        print('Erro ao tentar obter eventos da página')
        print(err)

# def salvar_data(data_str: str):
    # data_partes = data_str.split(',')
    
    # #data única
    # if len(data_partes) > 1:
    
    # #data com período 
    # else:
    #     data_partes = data_str.split(' a ')
encontrar_eventos()


#pegar cada link de evento
#entrar no link e pegar os dados para salvar
#criar os endpoints para retornar as consultas


#metadados
# preco
# local
# data inicio
# hora inicio
# data fim
# hora fim
# local aberto
# produtor
# descricao
# classificação indicativa