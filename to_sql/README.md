# to_sql
### Descrição
Script criado com o intuito de ler arquivos .csv e .xlsx e armazená-los no PostgreSQL, a fim de facilitar as análises.
O banco de dados onde fiz os testes foi criado no https://www.elephantsql.com/, gratuito e de 20 MB.
### Instalação
Para a utilização do script, será necessário instalar e importar essas três bibliotecas.
````
pip install psycopg2
pip install pandas
pip install sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
````
### Uso
Após instalar e importar as bibliotecas, será necessário anexar os parâmetros às seguintes variáveis: 
````
database = ""
user = ""
host= ""
password = ""
port = 1234
````
Em seguida, é necessário colocar o caminho de onde está esse arquivo em sua máquina na variável "caminho", o nome do arquivo na variável "nome" e o formato (.csv ou .xlsx) na variável "formato".
````
caminho = 'path'
nome = 'name'
formato = 'format'
````
Por fim, ao executar a célula abaixo, ela irá criar conexão com o banco e subir o arquivo do seu computador para o SQL.
Lembrando que o nome do arquivo em sua máquina será o mesmo da tabela no banco.
````
with create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}').connect() as connection:
    df = pd.read_excel(f'{caminho}{nome}{formato}')
    
    df.to_sql(f'{nome}', connection, if_exists='replace', index=False)
````

