from limite.tela_curso import TelaCurso
from entidade.curso import Curso
from entidade.cursoDAO import CursoDAO

class ControladorCurso():

  def __init__(self, controlador_sistema):
    self.__cursos = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema
    self.__curso = CursoDAO()

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
      self.__tela_curso.lista_curso({"opcao": str(len(cursos)) + ' - ' + curso.nome})
      cursos.append(curso.nome)
    escolhido = cursos[self.__tela_curso.seleciona_curso()]

    opcao = self.__tela_curso.opcoes_curso()
    if opcao == 1:
      self.__curso.remove(escolhido)
    elif opcao == 2:
      escolha = self.__tela_curso.opcoes_editar()
      if escolha == 1:
        curso.nome = self.__tela_curso.novo_campo()
      if escolha == 2:
        curso.instituicao = self.__tela_curso.novo_campo()

  def relatorio_curso(self):
    for curso in self.__curso.get_all():
      self.__tela_curso.mostra_curso({"nome": curso.nome,"instituicao": curso.instituicao })

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_curso, 2: self.operacoes_curso, 3: self.relatorio_curso, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()