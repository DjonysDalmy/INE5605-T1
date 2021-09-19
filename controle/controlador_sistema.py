from limite.tela_sistema import TelaSistema
from controle.controlador_curso import ControladorCurso
from controle.controlador_disciplina import ControladorDisciplina
from controle.controlador_professor import ControladorProfessor
from controle.controlador_aluno import ControladorAluno
from controle.controlador_atividade import ControladorAtividade
from exceptions.exc import TelaInvalidaException

class ControladorSistema:
    __instance = None

    def __init__(self):
        self.__main_view = TelaSistema()
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno= ControladorAluno(self)
        self.__controlador_atividade = ControladorAtividade(self)

    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance 
    
    def run(self):
        (values) = self.__main_view.open()
        return values

    def inicializa_sistema(self):
        self.abre_tela()

    def curso(self):
        self.__controlador_curso.abre_tela()

    def professor(self):
        self.__controlador_professor.abre_tela()

    def disciplina(self):
        self.__controlador_disciplina.abre_tela()

    def aluno(self):
        self.__controlador_aluno.abre_tela()

    def atividade(self):
        self.__controlador_atividade.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def volta_menu(self):
        self.__main_view.reiniciar()              

    def abre_tela(self):
        lista_opcoes = {1: self.curso, 2: self.professor, 3: self.disciplina, 4: self.aluno,5: self.atividade, 0:self.encerra_sistema}
        continuar = True
        while continuar:
            opcao_escolhida = self.__main_view.open()
            self.__main_view.close()              
            num = int(opcao_escolhida[1][0])
            try:
                funcao_escolhida = lista_opcoes[num]
                funcao_escolhida() 
            except:
                raise TelaInvalidaException()