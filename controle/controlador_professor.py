from entidade import disciplina
from limite.tela_professor import TelaProfessor
from controle.controlador_disciplina import ControladorDisciplina
from entidade.professor import Professor
from exceptions.exc import IndexErradoException, TelaInvalidaException

class ControladorProfessor():

  def __init__(self, controlador_sistema):
    self.__professores = []
    self.__tela_professor = TelaProfessor()
    self.__controlador_sistema = controlador_sistema

  def index_em_professor(self, index):
    return index < len(self.__professores)

  def cadastrar_professor(self):
    dados_professor = self.__tela_professor.pega_dados_professor()
    professor_ja_criado = dados_professor["nome"] in self.__professores
    if (professor_ja_criado):
      print("Professor já criado")
    else: 
      professor = Professor(dados_professor["nome"], dados_professor["idade"])
      self.__professores.append(professor)
     
  def operacoes_professor(self):
    i = 0
    for professor in self.__professores:
      self.__tela_professor.lista_professor({"opcao": str(i) + ' - ' + professor.nome})
      i += 1
    escolhido = self.__tela_professor.seleciona_professor()
    if (self.index_em_professor(escolhido)):
      professor = self.__professores[escolhido]
      opcao = self.__tela_professor.opcoes_professor()
      if opcao == 1:
        self.__professores.remove(professor)
      elif opcao == 2:
        escolha = self.__tela_professor.opcoes_editar()
        if escolha == 1:
          novo = self.__tela_professor.novo_campo(2)
          professor.nome = novo
        if escolha == 2:
          novo = self.__tela_professor.novo_campo(1)
          professor.idade = novo
        else: 
          raise IndexErradoException()
      else: 
        raise IndexErradoException()
    else: 
      raise IndexErradoException()

  def listar_minhas_disciplinas(self):
    nome_professor = self.__tela_professor.pega_nome_professor()
    for d in self.__professores:
      if (d.nome == nome_professor):
        disciplinas = Professor.listar_disciplinas(d)
        self.__tela_professor.lista_disciplinas(disciplinas)

  def vincular_disciplina(self):
    i = 0
    for professor in self.__professores:
      self.__tela_professor.lista_professor({"opcao": str(i) + ' - ' + professor.nome})
      i += 1
    escolhido = self.__tela_professor.seleciona_professor()
    if (self.index_em_professor(escolhido)):
      disciplinas = ControladorDisciplina.listar_disciplinas()
      disciplina = self.__tela_professor.vincular_disciplina(disciplinas)
      print(disciplina, 'teste')
      Professor.incluir_disciplina(disciplina)

  def retornar(self):
    self.__tela_professor.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_professor, 2: self.operacoes_professor, 3: self.listar_minhas_disciplinas, 4: self.vincular_disciplina, 0: self.retornar}

    continua = True
    while continua:
      opcao_escolhida = self.__tela_professor.open()   
      num = int(opcao_escolhida[1][0])
      try:
        funcao_escolhida = lista_opcoes[num]
        funcao_escolhida() 
      except:
        raise TelaInvalidaException()