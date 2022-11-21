from enum import Enum
import math

class Gerador:
    a
    c
    m
    x

    def __init__(self, semente):
        self.x = semente
        self.m = math.pow(2, 32)
        self.a = 1103515245
        self.c = 12345
    
    def next(self):
        x = ((self.a * self.x + self.c) / self.m)
        return x / self.m


class TipoEvento(Enum):
    CHEGADA: "CHEGADA"
    PASSAGEM: "PASSAGEM"
    SAIDA: "SAIDA"