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

    def test_quando_5_entrar_na_fila_5_deve_estar_no_final_da_fila(self):
        """Método testa quando 5 esta no final da fila"""
        entrada = 5
        saida_esperada = 5

        fila = Fila()

        # quando 5 entrar na fila  
        fila.entrar(entrada)
        
        # erro 
        # fila.entrar(10)

        # então 5 deve estar na fila
        # assertin para verificar se esta dentro
        self.assertEqual(saida_esperada, fila[-1])
    
    def test_quando_10_entrar_na_fila_10_deve_estar_no_final_da_fila(self):
        """Método testa quando 10 esta no final da fila"""
        entrada = 10    
        saida_esperada = 10 

        fila = Fila()

        # quando 10 entrar na fila  
        fila.entrar(entrada)
        
        # erro 
        # fila.entrar(20)

        # então 10 deve estar na fila
        # assertin para verificar se esta dentro
        self.assertEqual(saida_esperada, fila[-1])
