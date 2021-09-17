from entidade.aluno import Aluno
from entidade.atividade import Atividade

class Disciplina:
  def __init__(self, nome: str, limite_alunos: int):
    self.__alunos = []
    self.__nome = nome
    self.__limite_alunos = limite_alunos
    self.__responsaveis = []
    self.__atividades = []
    
  @property
  def responsaveis(self):
    return self.__responsaveis

  @responsaveis.setter
  def responsavel(self, responsavel):
    self.__responsaveis.append(responsavel)

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def limite_alunos(self):
    return self.__limite_alunos

  @limite_alunos.setter
  def limite_alunos(self, limite_alunos: int):
    self.__limite_alunos = limite_alunos

  @property
  def listar_alunos(self):
    return self.__alunos

  @listar_alunos.setter
  def incluir_aluno(self, aluno: Aluno):
    if aluno not in self.__alunos:
        self.__alunos.append(aluno)