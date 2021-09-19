import PySimpleGUI as sg

class TelaSistema:
    def __init__(self): 
        self.__window = None

    def init_components(self):
        layout = [
            [sg.Text('Escolha sua opção:')],
            [sg.Text('1 - Curso', size=(15, 1))],
            [sg.Text('2 - Professor', size=(15, 1))],
            [sg.Text('3 - Disciplina', size=(15, 1))],
            [sg.Text('4 - Aluno', size=(15, 1))],
            [sg.Text('5 - Atividade', size=(15, 1))],
            [sg.Text('0 - Desliga sistema', size=(15, 1))],
            [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
            [sg.Submit()]
        ]
        self.__window = sg.Window('Tela inicial sistema').Layout(layout)

    def open(self):
        self.init_components()
        values = self.__window.Read()
        return values

    def close(self): 
        self.__window.Close()
        
