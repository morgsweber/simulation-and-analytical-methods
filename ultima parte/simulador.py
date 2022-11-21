from resultados import *
from utils import *
from fila import *
from escalonador import *

class Simulador:
  estrutura_fila: List[Fila]
  sementes: List[int]
  alets: int
  primeira_chegada: List[Escalonador]

  def __init__(self, estrutura_fila: List[Fila], sementes: List[int], alets: int, primeira_chegada: List[Escalonador]):
    self.estrutura_fila = estrutura_fila
    self.sementes = sementes
    self.alets = alets
    self.primeira_chegada = primeira_chegada


  def inicia_simulacao(self):
    ids_fila: List[str] = ['']*len(self.estrutura_fila)
    tempos_estado: List[float] = []
    for i in range(len(self.estrutura_fila)):
      tempos_estado.append(List[float])
      ids_fila[i] = self.estrutura_fila[i].id
    resultados: Resultados = Resultados(ids_fila, 0.0, tempos_estado, [0.0]*len(self.estrutura_fila))
    for s in self.sementes:
      tempo: Resultados = self.inicia_simulacao(s, alets)
      resultados.soma_simulacao(tempo)
    resultados.reiniciareiniciar_simulacao(len(self.sementes))
    print(f"Resultados de {self.sementes} simulações:")
    print(f"{resultados}")

  def inicia_simulacao(self, semente_aleatoria, totalalets: int):
    comparador_agendamento: Escalonador
    agendamento: List
    for x in self.primeira_chegada:
      agendamento.append(x)
    num: Gerador = Gerador(semente_aleatoria)
    tempo: float = 0
    while (totalalets > 0):
      esc: Escalonador = agendamento.pop(0)
      variacao_tempo: float = esc.tempo - tempo
      for f in self.estrutura_fila:
        f.atualiza_tempo(variacao_tempo)
      tempo += variacao_tempo

      if (esc.evento == TipoEvento.CHEGADA):
        dest: Fila = esc.destino
        if not dest.esta_cheio:
          dest.add_cliente()
          if dest.agenda_servico_chegada:
            totalalets -= agenda_saida(agendamento, dest, tempo, num)
          else: dest.perda += 1
          agenda_chegada(agendamento, dest, tempo, num)
          totalalets-=1
        elif esc.evento == TipoEvento.PASSAGEM:
          origem: Fila = esc.origem
          dest: Fila = esc.destino
          origem.remove_cliente()
          if origem.agenda_servico_saida:
            totalalets -= agenda_saida(agendamento, origem, tempo, num)
          if not dest.esta_cheio:
            dest.add_cliente()
            if dest.agenda_servico_chegada:
              totalalets -= agenda_saida(agendamento, dest, tempo, num)
          else: dest.perda+=1
      else: 
        ori: Fila = esc.origem
        ori.remove_cliente()
        if ori.agenda_servico_saida:
          totalalets -= agenda_saida(agendamento, ori, tempo, num)
  
    tempo_filas:List[List[float]]
    perda: List[float] = [0.0] * len(self.estrutura_fila)
    ids_fila: List[str] = [''] * len(self.estrutura_fila)
    for i in range(len(self.estrutura_fila)):
      ids_fila[i] = self.estrutura_fila[i].id
      tempo_filas.append(self.estrutura_fila[i].tempos_estado)
      perda[i] = self.estrutura_fila[i].perda

    sr: Resultados = Resultados(ids_fila, tempo, tempo_filas, perda)
    for f in self.estrutura_fila:
      f.reiniciar_variaveis()
    return sr
    

  def agenda_chegada(self, escalonador, destino: Fila, tempo, alet: Gerador):
    numAlet: float = alet.next()
    evento_tempo = tempo + (destino.max_chegada - destino.min_chegada) * numAlet + destino.min_chegada
    escalonador.append(Escalonador.chegada(evento_tempo, destino))

  def agenda_saida(self, escalonador, origem: Fila, tempo, alet):
    numAlet = alet.next()
    aletsUsados = 1
    eventoTime = tempo + (origem.max_servico - origem.min_servico) * numAlet + origem.min_servico

    dest = None
    if(len(origem.destinos)) >1:
      randomProb = alex.next()
      aletsUsados += 1
      probabilidade = 0
      for i in range(len(origem.prob_destino)):
        probabilidade += origem.prob_destino[i]
        if randomProb < probabilidade:
          dest = origem.destinos[i]
          break
    else: dest = origem.destinos[0]
    if dest == Fila.FIM():
      escalonador.append(Escalonador.saida(eventoTime, origem))
    else: escalonador.append(Escalonador.passagem(eventoTime, origem, dest))
    return aletsUsados



