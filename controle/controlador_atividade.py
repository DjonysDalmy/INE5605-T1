from limite.tela_atividade import TelaAtividade
from entidade.atividade import Atividade
from controle.controlador_disciplina import ControladorDisciplina
from datetime import date

class ControladorAtividade():

  def __init__(self, controlador_sistema):
    self.__atividade = []
    self.__tela_atividade = TelaAtividade()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_atividade(self):
    ControladorDisciplina.listar_disciplinas()
    dados_atividade = self.__tela_atividade.pega_dados_atividade()
    atividade = Atividade(None, dados_atividade["titulo"], dados_atividade["descricao"], dados_atividade["prazo"], dados_atividade["disciplina"], None, False )

    self.__atividade.append(atividade)

  def visualizar_atividade(self):
    for atividade in self.__atividade:
      self.__tela_atividade.mostra_atividade({"titulo": atividade.titulo,"descricao": atividade.descricao,"prazo": atividade.prazo,"data_entregue": atividade.data_entregue,"entregue": atividade.entregue,"nota": atividade.nota})

  def operacoes_atividade(self):
    i = 0
    for atividade in self.__atividade:
      self.__tela_atividade.lista_atividade({"opcao": str(i) + ' - ' + atividade.titulo})
      i += 1
    atividade = self.__atividade[self.__tela_atividade.seleciona_atividade()]
    opcao = self.__tela_atividade.opcoes_atividade()
    if opcao == 1:
      self.__atividade.remove(atividade)
    elif opcao == 2:
      atividade.entregue = True
      atividade.data_entregue = date.today().strftime("%d/%m/%Y")
    elif opcao == 3:
      atividade.nota = self.__tela_atividade.corrigir()

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_atividade, 2: self.visualizar_atividade, 3: self.operacoes_atividade, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_atividade.tela_opcoes()]()