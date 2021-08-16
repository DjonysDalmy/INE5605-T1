class Atividade:
  def __init__(self, nota: int, titulo: str, descricao: str, prazo: str, data_entregue: str, entregue: bool):
    self.__nota = nota
    self.__titulo = titulo
    self.__descricao = descricao
    self.__prazo = prazo
    self.__data_entregue = data_entregue
    self.__entregue = entregue

  @property
  def nota(self):
    return self.__nota

  @nota.setter
  def nota(self, nota: int):
    self.__nota = nota

  @property
  def titulo(self):
    return self.__titulo

  @titulo.setter
  def descricao(self, titulo: str):
    self.__titulo = titulo

  @property
  def descricao(self):
    return self.__descricao

  @descricao.setter
  def descricao(self, descricao: str):
    self.__descricao = descricao

  @property
  def prazo(self):
    return self.__prazo

  @prazo.setter
  def prazo(self, prazo: str):
    self.__prazo = prazo

  @property
  def data_entregue(self):
    return self.__data_entregue

  @data_entregue.setter
  def data_entregue(self, data_entregue: str):
    self.__data_entregue = data_entregue

  @property
  def entregue(self):
    return self.__entregue

  @entregue.setter
  def entregue(self, entregue: bool):
    self.__entregue = entregue