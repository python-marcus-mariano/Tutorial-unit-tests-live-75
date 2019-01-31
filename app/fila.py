"""
Testes de unidades

Live de Python #75 - Testes de unidade

Homepage and documentation:


Copyright (c) 2019, Marcus Mariano.
License: MIT (see LICENSE for details)
"""


class Fila:
    """
    -> entrar:
        Enta sempre no final
    -> sair:
        Sai sempre no começo
    ."""
    
    def __init__(self):
        """Método """
        self.dado = []
    
    def __repr__(self):
        """Método """
        return f'{self.dado}'

    def entrar(self, valor):
        """Método Entrar"""
        self.dado.append(valor)
    
    def __getitem__(self, pos: int):
        """Método """
        return self.dado[pos]
