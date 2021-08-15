from limite.tela_curso import TelaCurso
from entidade.curso import Curso

class ControladorCurso():

  def __init__(self, controlador_sistema):
    self.__curso = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    curso = Curso(dados_curso["nome"])
    self.__curso.append(curso)

  def relatorio_curso(self):
    for curso in self.__curso:
      self.__tela_curso.mostra_curso({"nome": curso.nome,})

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_curso, 2: self.relatorio_curso, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()