from limite.tela_sistema import TelaSistema
from controle.controlador_curso import ControladorCurso

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def curso(self):
        self.__controlador_curso.abre_tela()

    def professor(self):
        print('b')

    def disciplina(self):
        print('b')

    def aluno(self):
        print('c')

    def atividade(self):
        print('d')

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.curso, 2: self.professor, 3: self.disciplina, 4: self.aluno,5: self.atividade, 0:self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()