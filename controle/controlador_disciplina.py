from limite.tela_aluno import TelaAluno
from limite.tela_atividade import TelaAtividade
from limite.tela_disciplina import TelaDisciplina
from entidade.aluno import Aluno
from entidade.disciplina import Disciplina

class ControladorDisciplina():

  def __init__(self, controlador_sistema):
    self.__disciplinas = []
    self.__tela_aluno = TelaAluno()
    self.__tela_atividades = TelaAtividade()
    self.__tela_disciplina = TelaDisciplina()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_disciplina(self):
    dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
    disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["limite_alunos"])
    self.__disciplinas.append(disciplina)

  def listar_disciplinas(self):
      return self.__disciplinas

  def listar_alunos_disciplina(self):
    index = 1
    nome_disciplina = self.__tela_disciplina.pega_nome_disciplina()
    disciplinas = listar_disciplinas()
    for d in self.disciplinas:
        if (nome_disciplina == d.nome):
          Disciplina.listar_alunos(d)
    
  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_disciplina, 2: self.listar_alunos_disciplina, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_disciplina.tela_opcoes()]()