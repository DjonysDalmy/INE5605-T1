from entidade.atividade import Atividade
from entidade.pessoa import Pessoa

class Aluno(Pessoa):
  def __init__(self, nome: str, idade: int):
    super().__init__(nome, idade)
    self.__atividades = []

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