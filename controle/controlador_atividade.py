from limite.tela_atividade import TelaAtividade
from entidade.atividade import Atividade

class ControladorAtividade():

  def __init__(self, controlador_sistema):
    self.__atividade = []
    self.__tela_atividade = TelaAtividade()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_atividade(self):
    dados_atividade = self.__tela_atividade.pega_dados_atividade()
    atividade = Atividade(None, dados_atividade["titulo"], dados_atividade["descricao"], dados_atividade["prazo"], None, False )
    self.__atividade.append(atividade)

  def visualizar_atividade(self):
      print('a')

  def operacoes_atividade(self):
      print('a')

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_atividade, 2: self.visualizar_atividade, 3: self.operacoes_atividade, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_atividade.tela_opcoes()]()