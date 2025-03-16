import sys
import mariadb


# Tabelas
# Cidades (Id, Nome, Estado)
# Categorias (Id, Descricao)
# Eventos (id, nome, tipo, IdCidade)
# DadosEventos ( Id, Id do evento, data, hora, local)
# Metadados
# tipoMetadados

def db_conexao(database = None):
    try:
        if database == None:
            conn = mariadb.connect(
                user="root",
                password="example",
                host="localhost",
                port=3306,
            )
            return conn
        else:
            conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3306,
            database=database
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def eventos_db():
    return db_conexao('eventos')

def criar_banco_de_dados():
    try:
        query = '''
            CREATE DATABASE IF NOT EXISTS `eventos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
            '''
        cursor = db_conexao().cursor()
        cursor.execute(query)
        cursor.connection.commit()
        cursor.connection.close()
    except Exception as err:
        print(err)
        print('Erro ao criar o banco de dados.')

def criar_tabelas():
    cidades = '''
        CREATE TABLE IF NOT EXISTS cidade(
            id int(11) NOT NULL AUTO_INCREMENT,
            nome varchar(50) NOT NULL,
            link varchar(50) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE(nome)
        ); 
    '''

    categorias = '''
        CREATE TABLE IF NOT EXISTS categoria(
            id int(11) NOT NULL AUTO_INCREMENT,
            nome varchar(50) NOT NULL,
            link varchar(50) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE(nome)
        )
    '''

    eventos = '''
        CREATE TABLE IF NOT EXISTS evento(
            id int(11) NOT NULL AUTO_INCREMENT,
            nome varchar(200) NOT NULL,
            site_id varchar(15) NOT NULL,
            categoria_id int(11) NULL,
            cidade_id int(11) NOT NULL,
            PRIMARY KEY (id),
            CONSTRAINT categoria_id_Fk FOREIGN KEY (categoria_id) REFERENCES categoria (id),
            CONSTRAINT cidade_id_Fk FOREIGN KEY (cidade_id) REFERENCES cidade (id)
        )
    '''
    
    tipo_metadados = '''
        CREATE TABLE IF NOT EXISTS tipo_metadado(
            id int(11) NOT NULL AUTO_INCREMENT,
            descricao VARCHAR(100) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE(descricao)
        )
    '''
    
    metadados = '''
        CREATE TABLE IF NOT EXISTS metadado(
            id int(11) NOT NULL AUTO_INCREMENT,
            valor varchar(10000) NOT NULL,
            data DATETIME NOT NULL DEFAULT NOW(),
            evento_id int(11) NOT NULL,
            tipo_metadado_id int(11) NOT NULL,
            PRIMARY KEY (id),
            CONSTRAINT evento_Fk FOREIGN KEY (evento_id) REFERENCES evento (id),
            CONSTRAINT tipo_metadado_Fk FOREIGN KEY (tipo_metadado_id) REFERENCES tipo_metadado (id)
        )
    '''
    try:
        cursor = eventos_db().cursor()
        cursor.execute(cidades)
        cursor.execute(categorias)
        cursor.execute(tipo_metadados)
        cursor.execute(eventos)
        cursor.execute(metadados)
        cursor.connection.commit()
        cursor.connection.close()
    except Exception as err:
        print('Erro ao realizar a criação das tabelas')
        print(err)

def criar_estrutura():
    criar_banco_de_dados()
    criar_tabelas()

def inserir_cidades(cidades):
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.executemany('INSERT IGNORE INTO cidade (nome, link) VALUES(%s, %s)', cidades)
        db.commit()
        db.close()
    except Exception as err:
        print('Erro ao inserir categorias')
        print(err)
 
def inserir_categorias(categorias):
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.executemany('INSERT IGNORE INTO categoria (nome, link) VALUES(%s, %s)', categorias)
        db.commit()
        db.close()
    except Exception as err:
        print('Erro ao inserir categorias')
        print(err)

def inserir_evento():
    db = eventos_db()

def inserir_metadado():
    db = eventos_db()


def obter_todas_cidades():
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM cidade')
        resultados = cursor.fetchall()
        return resultados
    except Exception as err:
        print('Erro ao obter todas as cidades')
        print(err)

def obter_todas_categorias():
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM categoria')
        resultados = cursor.fetchall()
        return resultados
    except Exception as err:
        print('Erro ao obter todas as categorias')
        print(err)

#excluir
def obter_cidade_por_nome(cidade):
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM cidade WHERE nome like %s', cidade)
        resultados = cursor.fetchall()
        return resultados
    except Exception as err:
        print('Erro ao obter todas as cidades')
        print(err)

def obter_categoria_por_nome(categoria):
    try:
        db = eventos_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM categoria WHERE nome like %s', categoria)
        resultados = cursor.fetchall()
        return resultados
    except Exception as err:
        print('Erro ao obter todas as cidades')
        print(err)
# identificar os tipos de metadados