"""Este arquivo contém tabelas para um banco de dados de gerenciamento de pedidos"""
import sqlite3
import pandas as pd

conn = sqlite3.connect('empresa_abc.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                ID_Cliente INTEGER PRIMARY KEY,
                Nome TEXT,
                Pais TEXT
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                ID_Produto INTEGER PRIMARY KEY,
                Nome_Produto TEXT,
                Categoria TEXT,
                Preco REAL
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                ID_Pedido INTEGER PRIMARY KEY,
                ID_Cliente INTEGER,
                Data_Pedido TEXT,
                FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
             )''')

c.execute('''CREATE TABLE IF NOT EXISTS Detalhes_Pedido (
                ID_Pedido INTEGER,
                ID_Produto INTEGER,
                Quantidade INTEGER,
                FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),
                FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)
             )''')

dados_clientes = [
   (1, 'João Silva', 'Brasil'),
   (2, 'Maria Garcia', 'Espanha'),
   (3, 'John Smith', 'EUA'),
   (4, 'Anna Müller', 'Alemanha'),
   (5, 'Luis Fernández', 'Argentina'),
   (6, 'Sophie Dupont', 'França'),
   (7, 'Mohammed Ali', 'Egito'),
   (8, 'Chen Wei', 'China'),
   (9, 'Haruto Tanaka', 'Japão'),
   (10, 'Olga Petrova', 'Rússia'),
   (11, 'Carlos Santos', 'Portugal'),
   (12, 'Fatima Khan', 'Paquistão'),
   (13, 'Javier Martinez', 'México'),
   (14, 'Emily Smith', 'Reino Unido'),
   (15, 'Giuseppe Rossi', 'Itália'),
   (16, 'Kim Min-ji', 'Coreia do Sul'),
   (17, 'Anna Novak', 'Polônia'),
   (18, 'Aliyah Khan', 'Índia'),
   (19, 'Miguel Rodríguez', 'Colômbia'),
   (20,'Elena Ivanova', 'Ucrânia'),
]

dados_produtos = [
   (101, 'Camisa', 'Vestuário', 20.00),
   (102, 'Tênis', 'Calçados', 50.00),
   (103, 'Calça Jeans', 'Vestuário', 30.00),
   (104, 'Óculos de Sol', 'Acessórios', 25.00),
   (105, 'Notebook', 'Eletrônicos', 800.00),
   (106, 'Bola de Futebol', 'Esportes', 10.00),
   (107, 'Colar', 'Acessórios', 35.00),
   (108, 'Fone de Ouvido', 'Eletrônicos', 50.00),
   (109, 'Sapatênis', 'Calçados', 45.00),
   (110, 'Câmera Fotográfica', 'Eletrônicos', 600.00),
   (111, 'Chapéu', 'Acessórios', 12.00),
   (112, 'Mochila', 'Acessórios', 40.00),
   (113, 'Jaqueta de Couro', 'Vestuário', 120.00),
   (114, 'Relógio', 'Acessórios', 60.00),
   (115, 'Skate', 'Esportes', 80.00),
   (116, 'Terno', 'Vestuário', 150.00),
   (117, 'Bicicleta', 'Esportes', 300.00),
   (118, 'Perfume', 'Beleza', 45.00),
   (119, 'Panela de Pressão', 'Casa', 50.00),
   (120, 'Cafeteira', 'Casa', 35.00),
]

dados_pedidos = [
   (501, 1, '2024-04-15'),
   (502, 2, '2024-04-16'),
   (503, 3, '2024-04-17'),
   (504, 4, '2024-04-18'),
   (505, 5, '2024-04-19'),
   (506, 6, '2024-04-20'),
   (507, 7, '2024-04-21'),
   (508, 8, '2024-04-22'),
   (509, 9, '2024-04-23'),
   (510, 10, '2024-04-24'),
   (511, 11, '2024-04-25'),
   (512, 12, '2024-04-26'),
   (513, 13, '2024-04-27'),
   (514, 14, '2024-04-28'),
   (515, 15, '2024-04-29'),
   (516, 16, '2024-04-30'),
   (517, 17, '2024-05-01'),
   (518, 18, '2024-05-02'),
   (519, 19, '2024-05-03'),
   (520, 20, '2024-05-04')
]

dados_detalhes_pedido = [
   (501, 101, 2),
   (502, 102, 1),
   (503, 103, 1),
   (504, 104, 3),
   (505, 101, 1),
   (506, 102, 2),
   (507, 103, 2),
   (508, 104, 1),
   (509, 101, 3),
   (510, 102, 1),
   (511, 103, 1),
   (512, 104, 2),
   (513, 101, 2),
   (514, 102, 3),
   (515, 103, 2),
   (516, 104, 1),
   (517, 101, 1),
   (518, 102, 2),
   (519, 103, 1),
   (520, 104, 3)
]

c.executemany("INSERT INTO Clientes (ID_Cliente, Nome, Pais) VALUES (?, ?, ?)", dados_clientes)
c.executemany("INSERT INTO Produtos (ID_Produto, Nome_Produto, Categoria, Preco) VALUES (?, ?, ?, ?)", dados_produtos)
c.executemany("INSERT INTO Pedidos (ID_Pedido, ID_Cliente, Data_Pedido) VALUES (?, ?, ?)", dados_pedidos)
c.executemany("INSERT INTO Detalhes_Pedido (ID_Pedido, ID_Produto, Quantidade) VALUES (?, ?, ?)", dados_detalhes_pedido)

conn.commit()

#Análise de Clientes
# a. Quais são os top 5 países em número de clientes?
clientes_por_pais = pd.read_sql_query("SELECT Pais, COUNT(*) as Numero_de_Clientes FROM Clientes GROUP BY Pais ORDER BY Numero_de_Clientes DESC LIMIT 5", conn)

# b. Quantos clientes únicos realizaram mais de um pedido?
clientes_multiplos_pedidos = pd.read_sql_query("SELECT COUNT(DISTINCT ID_Cliente) as Num_Clientes_Multiplos FROM Pedidos GROUP BY ID_Cliente HAVING COUNT(*) > 1", conn)

# c. Qual é o valor médio de pedidos por cliente em cada país?
valor_medio_por_cliente_pais = pd.read_sql_query("SELECT Pais, AVG(Num_Pedidos) as Valor_Medio_Pedidos FROM (SELECT C.Pais, COUNT(P.ID_Pedido) as Num_Pedidos FROM Clientes C JOIN Pedidos P ON C.ID_Cliente = P.ID_Cliente GROUP BY C.Pais, P.ID_Cliente) GROUP BY Pais", conn)

# d. Quais são os 3 principais clientes em termos de valor total de pedidos?
top_clientes = pd.read_sql_query("SELECT ID_Cliente, COUNT(*) as Num_Pedidos FROM Pedidos GROUP BY ID_Cliente ORDER BY Num_Pedidos DESC LIMIT 3", conn)

print("Os 5 principais países em número de clientes:\n", clientes_por_pais)
print("Número de clientes únicos que farão mais de um pedido:", len(clientes_multiplos_pedidos))
print("Valor médio de pedidos por cliente em cada país:\n", valor_medio_por_cliente_pais)
print("Os 3 principais clientes em termos de valor total de pedidos:\n", top_clientes)

#Análise de Produtos
# a. Quais são as top 5 categorias de produtos mais vendidas?
top_categorias = pd.read_sql_query("""
    SELECT Categoria, COUNT(*) as Num_Vendas 
    FROM Produtos 
    GROUP BY Categoria 
    ORDER BY Num_Vendas DESC 
    LIMIT 5
    """, conn)

# b. Qual é o produto mais caro que foi vendido?
produto_mais_caro = pd.read_sql_query("""
    SELECT Nome_Produto, Preco 
    FROM Produtos 
    ORDER BY Preco DESC 
    LIMIT 1
    """, conn)

# c. Qual categoria de produto gera a maior receita?
categoria_maior_receita = pd.read_sql_query("""
    SELECT Categoria, SUM(Preco * Quantidade) as Receita
    FROM Produtos
    JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
    GROUP BY Categoria
    ORDER BY Receita DESC
    LIMIT 1
    """, conn)

# d. Quais são os top 3 produtos mais vendidos?
top_produtos_vendidos = pd.read_sql_query("""
    SELECT Nome_Produto, COUNT(*) as Num_Vendas
    FROM Produtos
    JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
    GROUP BY Produtos.ID_Produto
    ORDER BY Num_Vendas DESC
    LIMIT 3
    """, conn)

print("As top 5 categorias de produtos mais vendidas:\n", top_categorias)
print("O produto mais caro que foi vendido:\n", produto_mais_caro)
print("A categoria de produto que gera a maior receita:\n", categoria_maior_receita)
print("Os top 3 produtos mais vendidos:\n", top_produtos_vendidos)

conn.close()
