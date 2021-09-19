from abc import abstractmethod
from limite.tela_disciplina import TelaDisciplina
from entidade.disciplina import Disciplina
from exceptions.exc import IndexErradoException, TelaInvalidaException

class ControladorDisciplina():

  def __init__(self, controlador_sistema):
    self.__disciplinas = []
    self.__tela_disciplina = TelaDisciplina()
    self.__controlador_sistema = controlador_sistema

  def index_em_disciplinas(self, index):
    return index < len(self.__disciplinas)

  def cadastrar_disciplina(self):
    dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
    disciplina_ja_criada = dados_disciplina["nome"] in self.__disciplinas
    if (disciplina_ja_criada):
      print("Disciplina já criada")
    else: 
      disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["limite_alunos"])
      self.__disciplinas.append(disciplina)
    

  def operacoes_disciplina(self):
    i = 0
    for disciplina in self.__disciplinas:
      self.__tela_disciplina.lista_disciplina({"opcao": str(i) + ' - ' + disciplina.nome})
      i += 1
    escolhido = self.__tela_disciplina.seleciona_disciplina()
    if (self.index_em_disciplinas(escolhido)):
      disciplina = self.__disciplinas[escolhido]
      opcao = self.__tela_disciplina.opcoes_disciplina()
      if opcao == 1:
        self.__disciplinas.remove(disciplina)
      elif opcao == 2: 
        escolha = self.__tela_disciplina.opcoes_editar()
        if escolha == 1:
          novo = self.__tela_disciplina.novo_campo(1)
          disciplina.nome = novo
        if escolha == 2:
          novo = self.__tela_disciplina.novo_campo(2)
          disciplina.limite_alunos = novo
        else: 
          raise IndexErradoException()
      else: 
        raise IndexErradoException()
    else: 
      raise IndexErradoException()

  def listar_disciplinas(self):
    return self.__disciplinas
    
  def listar_atividades(self):
    i = 0
    for disciplina in self.__disciplinas:
      self.__tela_disciplina.lista_disciplina({"opcao": str(i) + ' - ' + disciplina.nome})
      i += 1
    escolhido = self.__tela_disciplina.seleciona_disciplina()
    for d in self.__disciplinas:
      if (d.nome == escolhido):
        atividades = Disciplina.listar_atividades(d)
        self.__tela_disciplina.lista_atividades(atividades)
    
  def retornar(self):
    self.__tela_disciplina.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_disciplina, 2: self.operacoes_disciplina, 3: self.listar_atividades, 0: self.retornar}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_disciplina.open()   
      num = int(opcao_escolhida[1][0])
      try:
        funcao_escolhida = lista_opcoes[num]
        funcao_escolhida() 
      except:
        raise TelaInvalidaException()