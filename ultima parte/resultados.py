from typing import List

class Resultados:
  id_fila: List[str]
  descricao: List[str]
  tempo_simulacao: float
  tempos_estados: List[List[float]]
  perda: List[float]

  def __init__(self, id_fila: str, tempo_simulacao: float, tempos_estado: List[List[float]], perda: List[float]):
    self.id_fila = id_fila
    self.tempo_simulacao = tempo_simulacao
    self.tempos_estados = tempos_estado
    self.perda = perda
  
  def __str__(self):
    result = ""
    for i in range(len(self.tempos_estados)):
      tempos_fila: List[float] = self.tempos_estados[i]
      result += f"Fila {self.id_fila[i]}"
      for j in range(len(tempos_fila)):
        result += f" Estado: {j}  Tempo: {self.tempos_fila[j]}  Probabilidade: {100*tempos_fila[j]/self.tempo_simulacao}"
      result += f" Perda: {self.perda[i]}"
    result += f" Tempo total de simulação {self.tempo_simulacao}"
    return result

def soma_simulacao(self, resultados: Resultados):
  tempo_simulacao += resultados.tempo_simulacao
  for i in range(len(self.tempos_estados)):
    self.perda[i] += resultados.perda[i]
    tempos_fila1: List[float] = self.tempos_estados[i]
    tempos_fila2: List[float] = resultados.tempo_simulacao[i]
    comparador_listas(tempos_fila1, tempos_fila2)
    for j in range(len(tempos_fila1)):
      tempos_fila1.index(j, tempos_fila1(j) + tempos_fila2(j))

def reiniciar_simulacao(self, n: int):
  self.tempo_simulacao /= n
  for i in range(len(self.tempos_estados)):
    self.perda[i] /= n
    tempo_estado: List[float] = self.tempos_estados[i]
    for j in range(len(tempo_estado)):
      tempo_estado.index(j, tempo_estado[j] / n)
  
def comparador_listas(lista1: List[float], lista2: List[float]):
  while len(lista1) < len(lista2):
    lista1.append(0.0)
  while len(lista2) < len(lista1):
    lista2.append(0.0)

