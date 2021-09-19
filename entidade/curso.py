
class Curso:
  def __init__(self, nome: str, instituicao: str):
    self.__nome = nome
    self.__instituicao = instituicao

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def instituicao(self):
    return self.__instituicao

  @instituicao.setter
  def instituicao(self, instituicao: str):
    self.__instituicao = instituicao