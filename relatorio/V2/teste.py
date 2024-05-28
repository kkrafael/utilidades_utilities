#!/usr/bin/env python
# coding: utf-8

# In[11]:


from datetime import date


# In[32]:


class Relatorio:
    def __init__(self, projeto_a, projeto_b):
        self.today = date.today()
        self.projeto_a = projeto_a
        self.lista_projeto = [projeto_a, projeto_b]
        self.projeto_s()
        self.valida_s()
        self.valida_error()
        
    def projeto_s(self):
        self.lista_1 = []
        for projeto in self.lista_projeto:
            self.lista_1.append(projeto) 
    
    def valida_s(self):
        self.lista_2, self.lista_3, self.lista_4 = [], [], []
        for projeto in self.lista_projeto:
            if projeto != '': #self.ok_a = ['', '✅']
                self.lista_2.append('')
            else:
                self.lista_2.append('✅')
                
            if projeto != '':
                self.lista_3.append('')
            else:
                self.lista_3.append('\n')
                
            if projeto != '':
                self.lista_4.append('Processos que falharam: ')
            else:
                self.lista_4.append('')
    
    def valida_error(self):
        for projeto in self.lista_projeto:
            if projeto != '':
                self.erro = 'Ja estamos analisando o(s) erro(s)'
                break
            else:
                self.erro = '' 
        
    def gera_relatorio(self):
        texto = f'''
    Bom dia,

    Relatório do dia {self.today}

    Projeto a {self.lista_2[0]}
    {self.lista_4[0]}{self.lista_1[0]}{self.lista_3[0]}

    Projeto b {self.lista_2[1]}
    {self.lista_4[1]}{self.lista_1[1]}{self.lista_3[1]}
    
    {self.erro}

            '''
        return texto

