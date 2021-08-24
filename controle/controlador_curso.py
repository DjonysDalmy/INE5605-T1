from limite.tela_curso import TelaCurso
from entidade.curso import Curso

class ControladorCurso():

  def __init__(self, controlador_sistema):
    self.__cursos = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema

  def index_em_curso(self, index):
    return index < len(self.__cursos)

  def cadastrar_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    curso_ja_criado = dados_curso["nome"] in self.__cursos
    if (curso_ja_criado):
      print("Curso já criado")
    else: 
      curso = Curso(dados_curso["nome"])
      self.__cursos.append(curso)
    
  def operacoes_curso(self):
    i = 0
    for curso in self.__cursos:
      self.__tela_curso.lista_curso({"opcao": str(i) + ' - ' + curso.nome})
      i += 1
    escolhido = self.__tela_curso.seleciona_curso()
    if (self.index_em_curso(escolhido)):
      curso = self.__cursos[escolhido]
      opcao = self.__tela_curso.opcoes_curso()
      if opcao == 1:
        self.__cursos.remove(curso)
      elif opcao == 2:
        escolha = self.__tela_curso.opcoes_editar()
        if escolha == 1:
          curso.nome = self.__tela_curso.novo_campo()
    else: 
      print("Opcão de curso não existente")

  def relatorio_curso(self):
    for curso in self.__cursos:
      self.__tela_curso.mostra_curso({"nome": curso.nome,})

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_curso, 2: self.operacoes_curso, 3: self.relatorio_curso, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()