from limite.tela_professor import TelaProfessor
from limite.tela_atividade import TelaAtividade
from entidade.professor import Professor

class ControladorProfessor():

  def __init__(self, controlador_sistema):
    self.__professores = []
    self.__tela_professor = TelaProfessor()
    self.__controlador_sistema = controlador_sistema

  def index_em_professor(self, index):
    return index < len(self.__professores)

  def cadastrar_professor(self):
    dados_professor = self.__tela_professor.pega_dados_professor()
    professor = Professor(dados_professor["nome"], dados_professor["idade"])
    self.__professores.append(professor)

  def operacoes_professor(self):
    i = 0
    for professor in self.__professores:
      self.__tela_professor.lista_professor({"opcao": str(i) + ' - ' + professor.nome})
      i += 1
    escolhido = self.__tela_professor.seleciona_professor()
    if (self.index_em_professor(escolhido)):
      professor = self.__professores[escolhido]
      opcao = self.__tela_professor.opcoes_professor()
      if opcao == 1:
        self.__professores.remove(professor)
      elif opcao == 2:
        escolha = self.__tela_professor.opcoes_editar()
        if escolha == 1:
          novo = self.__tela_professor.novo_campo(2)
          professor.nome = novo
        if escolha == 2:
          novo = self.__tela_professor.novo_campo(1)
          professor.idade = novo
    else: 
      print("Opcão de professor não existente")

  def listar_minhas_disciplinas(self, disciplinas, nome):
    index = 1
    for disciplina in disciplinas:
        if (disciplina.regente == nome):
            print(index + "- "+ disciplina.nome)
            index += 1

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_professor, 2: self.operacoes_professor, 3: self.listar_minhas_disciplinas, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_professor.tela_opcoes()]()