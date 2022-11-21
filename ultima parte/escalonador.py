from fila import Fila
from utils import TipoEvento

class Escalonador:
  def __init__ (self, evento: TipoEvento, tempo: float, origem: Fila, destino: Fila):
    self.evento = evento
    self.tempo = tempo
    self.origem = origem
    self.destino = destino

  def __lt__(self, other):
    return self.tempo < other.tempo

  def __gt__(self, other):
    return self.tempo > other.tempo

  def __eq__(self, other):
    return self.tempo == other.tempo


  def chegada(tempo: float, destino: Fila):
    return Escalonador(TipoEvento.CHEGADA, tempo=tempo, origem=None, destino=destino)

  def saida(tempo: float, origem: Fila):
    return Escalonador(TipoEvento.SAIDA, tempo=tempo, origem=origem, destino=Fila.FIM())

  def passagem(tempo: float, origem: Fila, destino: Fila):
    return Escalonador(TipoEvento.PASSAGEM, tempo, origem, destino)
