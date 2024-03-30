# to_sql
### Descrição
Script criado com o intuito de ler aquivos csv e xlsx e armazena-los no PostgreSQL, afim de facilitar as análises.
O banco de dados onde fiz os teste foi criado no https://www.elephantsql.com/ de graça, de 20 MB.

### Instalação
Para a utilização do script, será necessário instalar e importar essas três bibliotecas.
````
pip install psycopg2
pip install pandas
pip install sqlalchemy
````
### Uso
Após instalar e importas as bibliotecas, será necessário anexar os parâmetros as seguintes variáveis: 
````
database = ""
user = ""
host= ""
password = ""
port = 1234
````
Em seguida, necessário colocar o caminho de onde está esse arquivo em sua máquina em "caminho", o nome do arquivo em "nome" e o formato (.csv ou .xlsx) em "formato" .
````
caminho = 'path'
nome = 'name'
formato = 'format'
````
Por fim executar essa ultima celula, ela irá criar conexão com o banco e subir o arquivo do seu computador para o sql.
Lembrando que nome do arquivo em seu pc, será o mesmo da tabela no banco.
````
with create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}').connect() as connection:
    df = pd.read_excel(f'{caminho}{nome}{formato}')
    
    df.to_sql(f'{nome}', connection, if_exists='replace', index=False)
````

