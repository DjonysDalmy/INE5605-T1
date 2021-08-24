from limite.tela_aluno import TelaAluno
from entidade.aluno import Aluno

class ControladorAluno():

  def __init__(self, controlador_sistema):
    self.__alunos = []
    self.__tela_aluno = TelaAluno()
    self.__controlador_sistema = controlador_sistema

  def index_em_alunos(self, index):
    return index < len(self.__alunos)

  def cadastrar_aluno(self):
    dados_aluno = self.__tela_aluno.pega_dados_aluno()
    alunoJahCriado = dados_aluno["nome"] in self.__alunos
    if (alunoJahCriado):
      print("Aluno já criado")
    else: 
      aluno = Aluno(dados_aluno["nome"], dados_aluno["idade"])
      self.__alunos.append(aluno)

  def operacoes_aluno(self):
    i = 0
    for aluno in self.__alunos:
      self.__tela_aluno.lista_aluno({"opcao": str(i) + ' - ' + aluno.nome})
      i += 1
    escolhido = self.__tela_aluno.seleciona_aluno()
    if (self.index_em_alunos(escolhido)):
      aluno = self.__alunos[escolhido]
      opcao = self.__tela_aluno.opcoes_aluno()
      if opcao == 1:
        self.__alunos.remove(aluno)
      elif opcao == 2: 
        escolha = self.__tela_aluno.opcoes_editar()
        if escolha == 1:
          novo = self.__tela_aluno.novo_campo(2)
          aluno.nome = novo
        if escolha == 2:
          novo = self.__tela_aluno.novo_campo(1)
          aluno.idade = novo
    else: 
      print("Opcão de aluno não existente")

  def listar_minhas_disciplinas(self, disciplinas):
    index = 1
    nome_aluno = self.__tela_aluno.pega_nome_aluno()
    for disciplina in disciplinas:
      if (nome_aluno in disciplina.alunos):
        print(index + "- "+ disciplina.nome)
        index += 1

  def listar_minhas_atividades(self):
      nome_aluno = self.__tela_aluno.pega_nome_aluno()
      for a in self.__alunos:
        if (a.nome == nome_aluno):
            Aluno.listar_atividades(a)
    
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_aluno, 2: self.operacoes_aluno, 3: self.listar_minhas_disciplinas, 4: self.listar_minhas_atividades, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluno.tela_opcoes()]()