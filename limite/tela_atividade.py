import PySimpleGUI as sg

class TelaAtividade():
  def __init__(self): 
    self.__window = None
    self.__atividades = []

  def init_components(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Cadastrar atividade', size=(20, 1))],
      [sg.Text('2 - Operações da ativdade', size=(20, 1))],
      [sg.Text('0 - Voltar', size=(20, 1))],
      [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Tela atividades').Layout(layout)

  def open(self):
    self.init_components()
    values = self.__window.Read()
    return values

  def pega_dados_atividade(self):
    self.close()
    layout = [
      [sg.Text('Escolha os dados da atividade:')],
      [sg.Text('Titúlo:', size=(15, 1)), sg.InputText("", key="titulo")],
      [sg.Text('Descrição:', size=(15, 1)), sg.InputText("", key="descricao")],
      [sg.Text('Prazo:', size=(15, 1)), sg.InputText("", key="prazo")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Adicionar atividade').Layout(layout)
    values = self.__window.Read()
    self.__window.Close()
    return values[1]
  
  def seleciona_atividade(self):
    self.close()
    layout = [
      [sg.Text('Escolha a atividade:', size=(20, 1))]
    ]
    for atividade in self.__atividades:
      layout.append([sg.Text(atividade, size=(20, 1))])

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela atividade').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__atividades = []
    return int(num['opcao'])

  def opcoes_atividade(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Excluir atividade', size=(15, 1))],
      [sg.Text('2 - Entregar atividade', size=(20, 1))],
      [sg.Text('3 - Corrigir atividade', size=(20, 1))],
      [sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Escolher operação').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    return int(num['opcao'])

  def corrigir(self):
    layout = [
      [sg.Text('Qual a sua nota?:', size=(15, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Escolher nota').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    return int(num['opcao'])

  def lista_atividade(self, dados_atividades):
    self.__atividades.append(dados_atividades["opcao"])
  
  def close(self): 
    self.__window.Close()