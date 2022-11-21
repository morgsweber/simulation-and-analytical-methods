from typing import List, Final

class Fila:
  id: str
  servidores: int
  capacidade: int
  min_chegada: float
  max_chegada: float
  min_servico: float
  max_servico: float
  destinos: List
  prob_destino: List[float]
  estado_fila: int
  tempos_estado: List[float]
  perda: int

  def __init__(self, id: str, servidores: int, capacidade: int, min_chegada: float, max_chegada: float, min_servico: float, max_servico: float, destinos: List):
    self.id = id
    self.servidores = servidores
    self.capacidade = capacidade
    self.min_chegada = min_chegada
    self.max_chegada = max_chegada
    self.min_servico = min_servico
    self.max_servico = max_servico
    if not destinos: 
      self.destinos = [] 
    else: self.destinos = destinos
    self.prob_destino = []
    self.reiniciar_variaveis()

  def esta_cheio(self):
    return self.estado_fila >= self.capacidade

  def agenda_servico_chegada(self):
    return self.estado_fila <= self.servidores

  def agenda_servico_saida(self):
    return self.estado_fila >= self.servidores

  def add_cliente(self):
    self.estado_fila += 1
    if len(self.tempos_estado) < self.estado_fila+1:
      self.tempos_estado.append(0.0)

  def remove_cliente(self):
    self.estado_fila -= 1

  def FIM():
    return Fila("FIM", -1,-1,-1,-1,-1,-1,None);

  def atualiza_tempo(self, variacao_tempo: float):
    self.tempos_estado.insert(self.estado_fila, self.tempos_estado[self.estado_fila] + variacao_tempo)

  def reiniciar_variaveis(self):
    self.estado_fila = 0
    self.tempos_estado = []
    self.tempos_estado.append(0.0)
    self.perda = 0