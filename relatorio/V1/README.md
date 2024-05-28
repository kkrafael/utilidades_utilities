
# V1
### Importação
Para a utilização do notebook, será necessário importar apenas a biblioteca datetime.
````
from datetime import date
````
### Uso
A primeira etapa para a automatização é atribuir a variável today a data do dia em que o notebook for rodar:
````
today = date.today(
````
Em seguida, precisamos criar variáveis de cada projeto que estamos analisando, e adicionar os processo que falharam, caso haja algum processo que tenha falhado.

````
processo_a = ''
processo_b = ''
processo_c = ''
````
Nessa etapa, caso exista mais projetos, será necessário fazer a seguinte adição "processo_xyz = ''.

Imediatamente após isso, teremos que ajustara condição se o projeto terá um ✅ ou se receberá o nome dos processos que falharam. 
````
#processo_a
if processo_a != '':
    ok_a = ''
    n_a = '\n'
    falha_a = 'Processos que falharam: '
else:
    ok_a = '✅'
    n_a = ''
    falha_a = ''
````
O _if_ está relacionado quando há um processo que falhou, portando a variável ok_a não receberá o check, hávera um _enter_ e a mensagem "Processos que falharam", antes do nome dos processos falhos.
_Else_ ocorrerá caso aquele projeto não receba nem um processo, portanto não houve falhas, ele receberá apenas ✅.

Logo após isso, teremos a etapa que terá uma mensagem no final do relatório, sinalizando que esses processos que falharam ja estão sendo ajustados.
````
if processo_a != '' or processo_b != '' or processo_c != '':
    error = 'Ja estamos analisando o(s) erro(s)'
else:
    error = ''
````
Por fim, a estrutura do relátorio.
````
texto = f'''
Bom dia,

Relatório do dia {today}

projeto a {ok_a}
{falha_a} {processo_a} {n_a}
projeto b {ok_b}
{falha_b} {processo_b} {n_b}
projeto c {ok_c}
{falha_c} {processo_c} {n_c}

{error}

'''
````
Estamos usando uma _f string_ com três aspas simples antes e depois do texto, para que seja possível estruturar em mais de uma linha. Em seguida colocamos alguma saudação, caso seja necessário (Bom dia). Logo após, um texto, se ncessário, e nossa várivavel _today_ que foi criada nas primeiras linhas, ela deve estar entre {chaves} para que a _f string_ entenda que é uma variável.
Em seguida colocamos o nome do projeto, **sem {chaves}**, seguido das seguintes variáveis, **com {chaves}**, ok_nomeprojeto, falha_nomeprojeto, processo_nomeprojeto, n_nomeprojeto.

Feito todas essas etapas, basta printar o relatório
````
print(texto)
````
````

Bom dia,

Relatório do dia 2024-05-26

projeto a ✅
  
projeto b ✅
  
projeto c ✅
````


