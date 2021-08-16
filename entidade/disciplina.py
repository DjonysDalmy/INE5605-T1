from aluno import Aluno

class Disciplina:
  def __init__(self, responsavel: str, limite_alunos: int):
    self.__alunos = []
    self.__limite_alunos = limite_alunos
    self.__responsavel = responsavel
    
  @property
  def responsavel(self):
    return self.__responsavel

  @responsavel.setter
  def responsavel(self, responsavel: str):
    self.__responsavel = responsavel

  @property
  def limite_alunos(self):
    return self.__limite_alunos

  @__limite_alunos.setter
  def limite_alunos(self, limite_alunos: int):
    self.__limite_alunos = limite_alunos

  @property
    def listar_alunos(self):
        return self.__alunos

  @alunos.setter
  def incluir_aluno(self, aluno: Aluno):
    if aluno not in self.__alunos:
        self.__alunos.append(aluno)