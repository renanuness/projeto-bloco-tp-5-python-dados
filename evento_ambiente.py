import re

palavras_evento_ceu_aberto = [
    "lounge",
    "praia",
    "corrida",
    "sunset",
    "festival",
    "feira",
    "picnic",
    "piquenique",
    "trilha",
    "caminhada",
    "acampamento",
    "camping",
    "passeio",
    "maratona",
    "skate",
    "patins",
    "bicicleta",
    "ciclismo",
    "surf",
    "kitesurf",
    "stand-up paddle",
    "yoga",
    "meditação",
    "observação de estrelas",
    "astronomia",
    "food truck",
    "open air",
    "ao ar livre",
    "jardim",
    "parque",
    "praça",
    "lago",
    "montanha",
    "cachoeira",
    "pôr do sol",
    "nascer do sol",
    "luau",
    "churrasco",
    "fogueira",
    "carnaval",
    "bloco de rua",
    "desfile",
    "graffiti",
    "cinema ao ar livre",
    "teatro de rua",
    "torneio",
    "oficina",
    "feira",
    "arena",
    "estádio coberto",
]

palavras_evento_ambiente_fechado = [
    "conferência",
    "palestra",
    "seminário",
    "congresso",
    "simpósio",
    "exposição",
    "mostra",
    "galeria",
    "museu",
    "teatro",
    "cinema",
    "baile",
    "salão"
    "auditório",
    "ginásio",
    "centro de convenções",
    "hotel",
    "restaurante",
    "bar",
    "boate",
    "clube",
    "festival de inverno",
    "ópera",
]

def tipo_ambiente_regex():
    ceu_aberto_regex = '\b'
    for i, val in enumerate(palavras_evento_ceu_aberto):
        ceu_aberto_regex += val
        if i != len(palavras_evento_ceu_aberto)-1:
            ceu_aberto_regex += '|'

    ceu_aberto_regex += '\b'

    ambiente_fechado_regex = '\b'
    for i, val in enumerate(palavras_evento_ambiente_fechado):
        ambiente_fechado_regex += val
        if i != len(palavras_evento_ambiente_fechado)-1:
            ambiente_fechado_regex += '|'

    ambiente_fechado_regex += '\b'

    return {'aberto':ceu_aberto_regex, 'fechado': ambiente_fechado_regex}

regexs = tipo_ambiente_regex()

def definir_tipo_ambiente(content: str):
    content = content.lower()
    aberto_matchs = re.findall(regexs['aberto'], content)
    fechado_matchs = re.findall(regexs['fechado'], content)

    if len(aberto_matchs) >= len(fechado_matchs):
        return 'aberto'
    
    return 'fechado'