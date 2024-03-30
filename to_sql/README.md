# to_sql
### Descrição

### Instalação
````
pip install psycopg2
pip install pandas
pip install sqlalchemy
````
### Uso
````
database = ""
user = ""
host= ""
password = ""
port = 1234
````

````
caminho = 'path'
nome = 'name'
formato = 'format'
````

````
with create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}').connect() as connection:
    df = pd.read_excel(f'{caminho}{nome}{formato}')
    
    df.to_sql(f'{nome}', connection, if_exists='replace', index=False)
````
