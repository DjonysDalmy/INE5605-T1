from limite.tela_aluno import TelaAluno
from limite.tela_atividade import TelaAtividade
from entidade.aluno import Aluno

class ControladorAluno():

  def __init__(self, controlador_sistema):
    self.__alunos = []
    self.__tela_aluno = TelaAluno()
    self.__tela_atividades = TelaAtividade()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_aluno(self):
    dados_aluno = self.__tela_aluno.pega_dados_aluno()
    aluno = Aluno(dados_aluno["nome"], dados_aluno["idade"])
    self.__alunos.append(aluno)

  def enviar_atividade(self):
    dados_atividade = self.__tela_atividades.pega_dados_atividade()
    atividade = Aluno.incluir_atividade(dados_atividade["nome"], dados_atividade["data_entrega"])

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
    lista_opcoes = {1: self.cadastrar_aluno, 2: self.enviar_atividade, 3: self.listar_minhas_disciplinas, 4: self.listar_minhas_atividades, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_aluno.tela_opcoes()]()