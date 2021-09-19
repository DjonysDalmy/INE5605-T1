from entidade.disciplina import Disciplina

class Professor:
  def __init__(self, nome: str, idade: int):
    self.__nome = nome
    self.__idade = idade
    self.__disciplinas = []

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def idade(self):
    return self.__idade

  @idade.setter
  def idade(self, idade: int):
    self.__idade = idade

  @property
  def disciplinas(self):
    return self.__disciplinas
 
  def incluir_disciplina(self, disciplina: Disciplina):
    if disciplina not in self.__disciplinas:
        self.__disciplinas.append(disciplina)

  def listar_disciplinas(self):
    return self.__disciplinas