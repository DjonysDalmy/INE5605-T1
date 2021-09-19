from entidade.dao import DAO
from entidade.curso import Curso

class CursoDAO(DAO):
  def __init__(self):
    super().__init__('curso.pkl')
  
  def add(self, curso: Curso):
    if curso is not None and isinstance(curso, Curso) and isinstance(curso.nome, str) and isinstance(curso.instituicao, str):
      super().add(curso.nome, curso)


  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)
  
  def remove(self, key: str):
    if isinstance(key, str):
      super().remove(key)