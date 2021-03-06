"""
Testes de unidades

Live de Python #75 - Testes de unidade

Homepage and documentation:


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""

from unittest import TestCase
from app.fila import Fila

class TestFila(TestCase):
    """TestCase."""  
    
    @classmethod
    def setUpClass(cls):
        """Fixture do classe - Método setupClass """
        print('setUpClass')
        cls.arquivo = 'arquivo.txt'
    
    @classmethod
    def tearDownClass(cls):
        """Fixture do classe - Método tearDownClass """
        print('tearDownClass')
        from os import remove
        # apagar o arquivo
        remove(cls.arquivo)

    def setUp(self):
        """Fixture do método - Método setup """
        print('setup')
        self.fila = Fila()
    
    def test_cria_arquivo(self):
        """Cirar arquivo"""
        print('criar arquvivo')
        open(self.arquivo, 'w')
        

    def tearDown(self):
        """Fixture do método - Método tearDown """        
        print('tearDown')

    def test_quando_5_entrar_na_fila_5_deve_estar_no_final_da_fila(self):
        """Método testa quando 5 esta no final da fila"""
        entrada = 5
        saida_esperada = 5
        
        # quando 5 entrar na fila  
        self.fila.entrar(entrada)

        # então 5 deve estar na fila
        # assertin para verificar se esta dentro
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)
    
    def test_quando_10_entrar_na_fila_10_deve_estar_no_final_da_fila(self):
        """Método testa quando 10 esta no final da fila"""
        entrada = 10    
        saida_esperada = 10 

        # quando 10 entrar na fila  
        self.fila.entrar(entrada)        

        # então 10 deve estar na fila
        # assertin para verificar se esta dentro
        self.assertEqual(saida_esperada, self.fila[-1])
        print(self.fila)
