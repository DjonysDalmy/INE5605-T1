from limite.tela_atividade import TelaAtividade
from entidade.atividade import Atividade
from datetime import date
from exceptions.exc import TelaInvalidaException, IndexErradoException

class ControladorAtividade():

  def __init__(self, controlador_sistema):
    self.__atividade = []
    self.__tela_atividade = TelaAtividade()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_atividade(self):
    dados_atividade = self.__tela_atividade.pega_dados_atividade()
    atividade = Atividade(None, dados_atividade["titulo"], dados_atividade["descricao"], dados_atividade["prazo"], None, False )

    self.__atividade.append(atividade)

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
    else:
      raise IndexErradoException()

  def retornar(self):
    self.__tela_atividade.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_atividade, 2: self.operacoes_atividade, 0: self.retornar}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_atividade.open()   
      num = int(opcao_escolhida[1][0])
      try:
        funcao_escolhida = lista_opcoes[num]
        funcao_escolhida() 
      except:
        raise TelaInvalidaException()