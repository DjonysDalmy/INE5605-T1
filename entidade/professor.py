from entidade.disciplina import Disciplina
from entidade.pessoa import Pessoa

class Professor(Pessoa):
  def __init__(self, nome: str, idade: int):
    super().__init__(nome, idade)
    self.__disciplinas = []

  @property
  def disciplinas(self):
    return self.__disciplinas
 
  def incluir_disciplina(self, disciplina: Disciplina):
    if disciplina not in self.__disciplinas:
        self.__disciplinas.append(disciplina)

  def listar_disciplinas(self):
    return self.__disciplinas