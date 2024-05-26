# Padronização de relatório
### Descrição
Estes notebook's foram criados com o intuito de automatizar relatórios diários. Pode ser utilizado para qualquer tarefa que seja interessante a padronização de informações (seja para controle pessoal ou repasse).

Os notebooks geram um relatório padronizado informando os processos que falharam e/ou que tiveram sucesso dentro de cada projeto. Dessa forma, ele altera a data para a data atual, e após a inserção dos processos que falharam, gera o relatório com essas informações no campo adequado do sucesso ou falha.

Caso não tenha nem uma falha, o notebook irá retornar um check para todos os projetos.
Exemplo:
````
Bom dia,

Relatório do dia 2024-05-26

projeto a ✅
  
projeto b ✅
  
projeto c ✅
````

Caso haja pelo menos um processo com falha, o notebook irá trazer junto ao nome do projeto, os processos que falharam, sem o check, e irá retornar a seguinte mensagem: "Ja estamos analisando o(s) erro(s)". Os projetos que rodaram sem erros continuarão com o check.
Exemplo:
````
Bom dia,

Relatório do dia 2024-05-26

projeto a 
Processos que falharam:  linha 1 

projeto b ✅
  
projeto c 
Processos que falharam:  linha 1, linha 4 

Ja estamos analisando o(s) erro(s)
````

Vou deixar todos as versões que fiz desse relatório para quem quiser e precisar usar, com instruções de como adicionar novos processos.

