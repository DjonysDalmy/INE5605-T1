from limite.tela_curso import TelaCurso
from entidade.curso import Curso
from exceptions.exc import IndexErradoException, TelaInvalidaException
from entidade.cursoDAO import CursoDAO

class ControladorCurso():

  def __init__(self, controlador_sistema):
    self.__cursos = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema
    self.__curso = CursoDAO()
    self.adiciona_cursos_salvos()

  def adiciona_cursos_salvos(self):
    for curso in self.__curso.get_all():
      self.__cursos.append(curso)

  def index_em_curso(self, index):
    return index < len(self.__curso.get_all())

  def cadastrar_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    if (dados_curso["nome"] in self.__cursos):
      print("Curso já criado")
    else:
      self.__curso.add(Curso(dados_curso["nome"], dados_curso["instituicao"]))
    
  def operacoes_curso(self):
    cursos = []
    for curso in self.__curso.get_all():
      cursos.append(curso)

    escolhido = self.__tela_curso.seleciona_curso(cursos)
    if (self.index_em_curso(escolhido)):
      curso = self.__cursos[escolhido]
      opcao = self.__tela_curso.opcoes_curso()
      if opcao == 1:
        self.__cursos.remove(curso)
        self.__curso.remove(curso)
      elif opcao == 2:
        escolha = self.__tela_curso.opcoes_editar()
        if escolha == 1:
          curso.nome = self.__tela_curso.novo_campo(1)
        if escolha == 2:
          curso.instituicao = self.__tela_curso.novo_campo(2)
        else: 
          raise IndexErradoException()
      else: 
        raise IndexErradoException()
    else: 
      raise IndexErradoException()

  def relatorio_curso(self):
    cursos = []
    for curso in self.__curso.get_all():
      cursos.append(curso)
    self.__tela_curso.relatorio_curso(cursos)

  def retornar(self):
    self.__tela_curso.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_curso, 2: self.operacoes_curso, 3: self.relatorio_curso, 0: self.retornar}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_curso.open()   
      num = int(opcao_escolhida[1][0])
      try:
        funcao_escolhida = lista_opcoes[num]
        funcao_escolhida() 
      except:
        raise TelaInvalidaException()
