# Simulator-Telos (Introdução à manipulação de dados com Python e SQL)

### Contextualização
Exercício realizado para o programa Telos cujo principal objetivo é aprofundar-se no mundo da manipulação de dados utilizando um
combinação de Python, SQL e técnicas de análise de dados.

### Descrição
A Empresa ABC é uma varejista online que vende uma variedade de produtos, desde eletrônicos até vestuário. Eles operam em vários países e têm uma base de clientes diversificada. Recentemente, a empresa decidiu analisar seu banco de dados de vendas para melhor entender o comportamento do cliente, identificar produtos de alta demanda e otimizar suas operações de vendas. Para isso, eles precisam analisar seus
dados de vendas, que incluem informações sobre clientes, pedidos, produtos e transações.

Dados Necessários

Clientes: ID do Cliente, Nome, País

Produtos:ID do Produto, Nome do Produto, Categoria, Preço

Pedidos:ID do Pedido, ID do Cliente, Data do Pedido

Detalhes do Pedido:ID do Pedido, ID do Produto, Quantidade

### Orientações para a Execução
1) Criação do Banco de Dados e Tabelas com SQLite:
   
● Use Python para criar um banco de dados SQLite chamado empresa_abc.db.

conn = sqlite3.connect('empresa_abc.db')

c = conn.cursor()

● Crie tabelas conforme descrito na seção "Descrição".

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
             

2) Geração de Dados com GPT e Inserção no SQLite:

● Utilize o GPT para gerar dados fictícios que se encaixem nos requisitos das
tabelas.

● Insira esses dados nas tabelas do banco de dados SQLite.

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


3) Leitura e Manipulação dos Dados com Pandas:
   
● Utilize pandas para ler os dados do banco de dados SQLite.

Instalando pandas com **pip install pandas** e depois importando desta forma i**mport pandas as pd**

● Realize as análises e responda às perguntas de negócio propostas nas seções

### Análise de Clientes
### a. Quais são os top 5 países em número de clientes?
clientes_por_pais = pd.read_sql_query("SELECT Pais, COUNT(*) as Numero_de_Clientes FROM Clientes GROUP BY Pais ORDER BY Numero_de_Clientes DESC LIMIT 5", conn)

### b. Quantos clientes únicos realizaram mais de um pedido?
clientes_multiplos_pedidos = pd.read_sql_query("SELECT COUNT(DISTINCT ID_Cliente) as Num_Clientes_Multiplos FROM Pedidos GROUP BY ID_Cliente HAVING COUNT(*) > 1", conn)

### c. Qual é o valor médio de pedidos por cliente em cada país?
valor_medio_por_cliente_pais = pd.read_sql_query("SELECT Pais, AVG(Num_Pedidos) as Valor_Medio_Pedidos FROM (SELECT C.Pais, COUNT(P.ID_Pedido) as Num_Pedidos FROM Clientes C JOIN Pedidos P ON C.ID_Cliente = P.ID_Cliente GROUP BY C.Pais, P.ID_Cliente) GROUP BY Pais", conn)

### d. Quais são os 3 principais clientes em termos de valor total de pedidos?
top_clientes = pd.read_sql_query("SELECT ID_Cliente, COUNT(*) as Num_Pedidos FROM Pedidos GROUP BY ID_Cliente ORDER BY Num_Pedidos DESC LIMIT 3", conn)


**print("Os 5 principais países em número de clientes:\n", clientes_por_pais)  --> Como cada país possui apenas um cliente de acordo com os dados de teste, a consulta SQL contou o número de clientes de cada país 
 Índia: 1, Ucrânia: 1, Rússia: 1, Reino Unido: 1 e Portugal: 1**

**print("Número de clientes únicos que farão mais de um pedido:", len(clientes_multiplos_pedidos)) --> Como cada cliente tem apenas um pedido nos dados de teste, a consulta não encontrará nenhum cliente que tenha feito mais de um pedido**

**print("Valor médio de pedidos por cliente em cada país:\n", valor_medio_por_cliente_pais) --> Cada cliente em cada país fez exatamente um pedido, então o valor médio é 1.0**

**print("Os 3 principais clientes em termos de valor total de pedidos:\n", top_clientes) --> Como nos dados de teste cada cliente tem apenas um pedido, o número de pedidos por cliente é 1 para todos.**


### Análise de Produtos
### a. Quais são as top 5 categorias de produtos mais vendidas?
top_categorias = pd.read_sql_query("""
   SELECT Categoria, SUM(Quantidade) AS Total_Vendas
FROM Produtos
JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
GROUP BY Categoria
ORDER BY Total_Vendas DESC
LIMIT 5;
   """, conn)

### b. Qual é o produto mais caro que foi vendido?
produto_mais_caro = pd.read_sql_query("""
   SELECT p.Nome_Produto
    FROM Produtos p
    JOIN Detalhes_Pedido dp ON p.ID_Produto = dp.ID_Produto
    GROUP BY p.ID_Produto
    ORDER BY MAX(p.Preco) DESC
    LIMIT 1;
    """, conn)

### c. Qual categoria de produto gera a maior receita?
categoria_maior_receita = pd.read_sql_query("""
    SELECT Categoria, SUM(Preco * Quantidade) as Receita
    FROM Produtos
    JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
    GROUP BY Categoria
    ORDER BY Receita DESC
    LIMIT 1
    """, conn)

### d. Quais são os top 3 produtos mais vendidos?
top_produtos_vendidos = pd.read_sql_query("""
    SELECT Nome_Produto, SUM(Quantidade) AS Total_Vendas
   FROM Produtos
   JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
   GROUP BY Produtos.ID_Produto
   ORDER BY Total_Vendas DESC
   LIMIT 3;

    """, conn)

**print("As top 5 categorias de produtos mais vendidas:\n", top_categorias) --> Vestuário 16, Acessórios 10 e  Calçados 9**

**print("O produto mais caro que foi vendido:\n", produto_mais_caro) --> Tênis**

**print("A categoria de produto que gera a maior receita:\n", categoria_maior_receita) --> Calçados 450.0**

**print("Os top 3 produtos mais vendidos:\n", top_produtos_vendidos) --> Óculos de Sol 10, Tênis 9 e  Camisa 9**

### Análise de Pedidos
### a. Qual é o número total de pedidos realizados por mês?

total_pedidos_mes = pd.read_sql_query("""
   SELECT strftime('%m', Data_Pedido) AS Mes, COUNT(*) AS Total_Pedidos
   FROM Pedidos
   GROUP BY Mes
   """, conn)
   
### b. Qual é o valor médio de um pedido?

valor_meio_pedido = pd.read_sql_query("""
   SELECT AVG(Preco_Total) AS Valor_Medio_Pedido
   FROM (
    SELECT ID_Pedido, SUM(Preco * Quantidade) AS Preco_Total
   FROM Produtos
   JOIN Detalhes_Pedido ON Produtos.ID_Produto = Detalhes_Pedido.ID_Produto
   GROUP BY ID_Pedido
   );                                   
   """, conn)
   
### c. Quais são os dias da semana com mais pedidos?

dia_semana_pedidos = pd.read_sql_query("""
   SELECT strftime('%w', Data_Pedido) AS Dia_Semana, COUNT(*) AS Total_Pedidos
   FROM Pedidos
   GROUP BY Dia_Semana
   ORDER BY Total_Pedidos DESC
   LIMIT 1
   """, conn)
   
### d. Qual é o país com o maior número de pedidos?

pais_maior_pedidos = pd.read_sql_query("""
   SELECT c.Pais, COUNT(*) AS Total_Pedidos
   FROM Pedidos p
   JOIN Clientes c ON p.ID_Cliente = c.ID_Cliente
   GROUP BY c.Pais
   ORDER BY Total_Pedidos DESC
   LIMIT 1
   """, conn)

**print("O número total de pedidos realizados por mês:\n", total_pedidos_mes) --> mês 04: 16 e mês 05: 4**

**print("O valor médio de um pedido:\n", valor_meio_pedido) -->  54.5**

**print("Os dias da semana com mais pedidos?:\n", dia_semana_pedidos) --> dia 6: 3**

**print("País com o maior número de pedidos:\n", pais_maior_pedidos) --> Índia 1 -- tendo em conta que todos os países têm o mesmo número de pedidos**


### Análise de Tendências de Vendas

### a. Como as vendas de cada categoria de produto mudaram ao longo do ano?

vendas_por_categoria = pd.read_sql_query ("""
   SELECT strftime('%m', P.Data_Pedido) AS Mes, Pr.Categoria, SUM(DP.Quantidade) AS Total_Vendas
   FROM Pedidos P
   JOIN Detalhes_Pedido DP ON P.ID_Pedido = DP.ID_Pedido
   JOIN Produtos Pr ON DP.ID_Produto = Pr.ID_Produto
   GROUP BY Mes, Pr.Categoria
   ORDER BY Mes, Pr.Categoria
""", conn)

### b. Existe alguma correlação entre o país do cliente e a categoria de produto comprada?

correlacao_pais_categoria = pd.read_sql_query("""
    SELECT C.Pais, Pr.Categoria, COUNT(*) AS Total
    FROM Clientes C
    JOIN Pedidos P ON C.ID_Cliente = P.ID_Cliente
    JOIN Detalhes_Pedido DP ON P.ID_Pedido = DP.ID_Pedido
    JOIN Produtos Pr ON DP.ID_Produto = Pr.ID_Produto
    GROUP BY C.Pais, Pr.Categoria
    """, conn)

### c. Como o valor médio do pedido varia por mês?

valor_medio_por_mes = pd.read_sql_query("""
   SELECT strftime('%m', P.Data_Pedido) AS Mes, AVG(Total_Pedido) AS Valor_Medio_Pedido
   FROM (
      SELECT DP.ID_Pedido, SUM(Pr.Preco * DP.Quantidade) AS Total_Pedido
      FROM Pedidos P
      JOIN Detalhes_Pedido DP ON P.ID_Pedido = DP.ID_Pedido
      JOIN Produtos Pr ON DP.ID_Produto = Pr.ID_Produto
      GROUP BY DP.ID_Pedido
   ) AS Subquery
   JOIN Pedidos P ON Subquery.ID_Pedido = P.ID_Pedido
   GROUP BY Mes
   ORDER BY Mes
""", conn)

### d. Qual categoria de produto mostra a maior variação de vendas entre os meses?

vendas_por_categoria = pd.read_sql_query("""
SELECT strftime('%m', P.Data_Pedido) AS Mes, Pr.Categoria, SUM(DP.Quantidade) AS Total_Vendas
   FROM Pedidos P
   JOIN Detalhes_Pedido DP ON P.ID_Pedido = DP.ID_Pedido
   JOIN Produtos Pr ON DP.ID_Produto = Pr.ID_Produto
   GROUP BY Mes, Pr.Categoria
   ORDER BY Mes, Pr.Categoria
""", conn)

**print("Vendas por categoria:\n", vendas_por_categoria) --> As vendas de cada categoria de produto ao longo do ano mostram uma variação significativa. No mês 04, a categoria "Vestuário" teve o maior número de vendas, seguida por "Acessórios" e "Calçados". No mês 05, houve uma redução nas vendas em todas as categorias, com "Acessórios" mantendo o maior número de vendas, seguido por "Calçados" e "Vestuário".
0  04  Acessórios             7
1  04    Calçados             7
2  04   Vestuário            14
3  05  Acessórios             3
4  05    Calçados             2
5  05   Vestuário             2**

**print("Correlação entre o país do cliente e a categoria de produto comprada:\n",correlacao_pais_categoria) -->  Cada país tem pelo menos uma compra em diferentes categorias de produtos, sem padrões óbvios de preferência por categoria de produto com base no país do cliente
            Pais     Categoria  Total
0        Alemanha  Acessórios      1
1       Argentina   Vestuário      1
2          Brasil   Vestuário      1
3           China  Acessórios      1
4        Colômbia   Vestuário      1
5   Coreia do Sul  Acessórios      1
6             EUA   Vestuário      1
7           Egito   Vestuário      1
8         Espanha    Calçados      1
9          França    Calçados      1
10         Itália   Vestuário      1
11          Japão   Vestuário      1
12         México   Vestuário      1
13      Paquistão  Acessórios      1
14        Polônia   Vestuário      1
15       Portugal   Vestuário      1
16    Reino Unido    Calçados      1
17         Rússia    Calçados      1
18        Ucrânia  Acessórios      1
19          Índia    Calçados      1**

**print("Valor médio do pedido varia por mês:\n", valor_medio_por_mes) --> Em abril, o valor médio do pedido foi de aproximadamente $54,06, enquanto em maio aumentou para cerca de $56,25.
 Mes  Valor_Medio_Pedido
0  04             54.0625
1  05             56.2500**

**print("Categoria de produto com maior variação de vendas:\n",variacao_vendas_por_categoria) -->  a categoria de produto que mostra a maior variação de vendas entre os meses é "Vestuário"
Mes  Categoria  Total_Vendas
05  Vestuário            16**

### Insights e Oportunidades

### a. Identifique os produtos que têm alta demanda, mas baixa disponibilidade em estoque.

produtos_alta_demanda_baixo_estoque = pd.read_sql_query("""
   SELECT p.Nome_Produto, p.Categoria, SUM(dp.Quantidade) AS Total_Vendido, p.Preco, 
      (SELECT COUNT(*) FROM Detalhes_Pedido WHERE ID_Produto = p.ID_Produto) AS Total_Encomendado
   FROM Produtos p
   JOIN Detalhes_Pedido dp ON p.ID_Produto = dp.ID_Produto
   GROUP BY p.ID_Produto
   HAVING Total_Vendido > Total_Encomendado
   """, conn)


### b. Quais são os países com maior potencial de expansão de mercado com base nos dados de vendas?

expansao_mercado_paises = pd.read_sql_query("""
   SELECT c.Pais, COUNT(DISTINCT pe.ID_Cliente) AS Clientes, COUNT(*) AS Total_Pedidos
   FROM Clientes c
   JOIN Pedidos pe ON c.ID_Cliente = pe.ID_Cliente
   GROUP BY c.Pais
   ORDER BY Total_Pedidos DESC
   """, conn)

### c. Analise a eficácia das promoções em termos de aumento no número de pedidos.


### d. Identifique padrões de compra recorrentes entre clientes.

eficacia_promocoes = pd.read_sql_query("""
   SELECT c.Nome, p.Nome_Produto, COUNT(*) AS Total_Pedidos 
   FROM Clientes c
   JOIN Pedidos pe ON c.ID_Cliente = pe.ID_Cliente
   JOIN Detalhes_Pedido dp ON pe.ID_Pedido = dp.ID_Pedido
   JOIN Produtos p ON dp.ID_Produto = p.ID_Produto
   GROUP BY c.Nome, p.Nome_Produto
   ORDER BY Total_Pedidos DESC
   """, conn)

**print("produtos que têm alta demanda, mas baixa disponibilidade em estoque:\n", produtos_alta_demanda_baixo_estoque) -->
Nome_Produto   Categoria                Total_Vendido        Preco              Total_Encomendado
 Camisa         Vestuário                  9                  20.0                  5
Tênis           Calçados                   9                  50.0                  5
Calça Jeans      Vestuário                 7                  30.0                  5
Óculos de Sol    Acessórios               10                  25.0                  5**


**print(" países com maior potencial de expansão de mercado:\n",expansao_mercado_paises) --> neste caso, tudo de acordo com os dados de teste
            Pais  Clientes  Total_Pedidos
0           Índia         1              1
1         Ucrânia         1              1
2          Rússia         1              1
3     Reino Unido         1              1
4        Portugal         1              1
5         Polônia         1              1
6       Paquistão         1              1
7          México         1              1
8           Japão         1              1
9          Itália         1              1
10         França         1              1
11        Espanha         1              1
12          Egito         1              1
13            EUA         1              1
14  Coreia do Sul         1              1
15       Colômbia         1              1
16          China         1              1
17         Brasil         1              1
18      Argentina         1              1
19       Alemanha         1              1**

#print(":\n", )


**print(": padrões de compra recorrentes entre clientes\n",eficacia_promocoes) --> neste caso, tudo de acordo com os dados de teste
                 Nome   Nome_Produto  Total_Pedidos
0        Aliyah Khan          Tênis              1
1        Anna Müller  Óculos de Sol              1
2         Anna Novak         Camisa              1
3      Carlos Santos    Calça Jeans              1
4           Chen Wei  Óculos de Sol              1
5      Elena Ivanova  Óculos de Sol              1
6        Emily Smith          Tênis              1
7        Fatima Khan  Óculos de Sol              1
8     Giuseppe Rossi    Calça Jeans              1
9      Haruto Tanaka         Camisa              1
10   Javier Martinez         Camisa              1
11        John Smith    Calça Jeans              1
12        João Silva         Camisa              1
13        Kim Min-ji  Óculos de Sol              1
14    Luis Fernández         Camisa              1
15      Maria Garcia          Tênis              1
16  Miguel Rodríguez    Calça Jeans              1
17      Mohammed Ali    Calça Jeans              1
18      Olga Petrova          Tênis              1
19     Sophie Dupont          Tênis              1**
