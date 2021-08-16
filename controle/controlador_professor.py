from limite.tela_professor import TelaProfessor
from limite.tela_atividades import TelaAtividade
from entidade.professor import Professor

class ControladorProfessor():

  def __init__(self, controlador_sistema):
    self.__professores = []
    self.__tela_professor = TelaProfessor()
    self.__tela_atividades = TelaAtividade()
    self.__controlador_sistema = controlador_sistema

  def cadastrar_professor(self):
    dados_professor = self.__tela_professor.pega_dados_professor()
    professor = Professor(dados_professor["nome"], dados_professor["idade"])
    self.__professores.append(professor)

  def cadastrar_atividade(self):
    dados_atividade = self.__tela_atividades.pega_dados_atividade()
    atividade = Atividade(dados_atividade["nome"], dados_atividade["data_entrega"])
    self.__professores.append(professor)

  def avaliar_atividade(self):
    dados_atividade = self.__tela_atividades.pega_dados_avaliar_atividade()
    atividade = Atividade(dados_atividade["nome"], dados_atividade["data_entrega"])
    self.__professores.append(professor)

  def listar_minhas_disciplinas(self, disciplinas, nome):
    index = 1
    for disciplina in disciplinas:
        if (disciplina.regente === nome):
            print(index + "- "+ disciplina.nome)
            index += 1

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_professor, 2: self.cadastrar_atividade, 3: self.listar_minhas_disciplinas, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_professor.tela_opcoes()]()