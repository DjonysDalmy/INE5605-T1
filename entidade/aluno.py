from entidade.atividade import Atividade

class Aluno:
  def __init__(self, nome: str, idade: int):
    self.__nome = nome
    self.__idade = idade
    self.__atividades = []

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
  def atividade(self):
    return self.__atividade

  @atividade.setter
  def incluir_atividade(self, atividade: Atividade):
    if atividade not in self.__atividades:
        self.__atividades.append(atividade)
    
  @property
  def listar_atividades(self):
    for atividade in self.__atividades:
      print(atividade.nome)