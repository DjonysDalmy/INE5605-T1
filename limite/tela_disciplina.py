import PySimpleGUI as sg

class TelaDisciplina():
  def __init__(self): 
    self.__window = None
    self.__disciplinas = []

  def init_components(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Cadastrar disciplina', size=(20, 1))],
      [sg.Text('2 - Operações da disciplina', size=(20, 1))],
      [sg.Text('3 - Listar atividades', size=(20, 1))],
      [sg.Text('0 - Voltar', size=(20, 1))],
      [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Tela disciplinas').Layout(layout)

  def open(self):
    self.init_components()
    values = self.__window.Read()
    return values

  def pega_dados_disciplina(self):
    self.close()
    layout = [
      [sg.Text('Escolha os dados da disciplina:')],
      [sg.Text('Nome da disciplina:', size=(15, 1)), sg.InputText("", key="nome")],
      [sg.Text('Limite de alunos:', size=(15, 1)), sg.InputText("", key="limite_alunos")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Adicionar disciplina').Layout(layout)
    values = self.__window.Read()
    self.__window.Close()
    return values[1]
  
  def seleciona_disciplina(self):
    self.close()
    layout = [
      [sg.Text('Escolha a disciplina:', size=(20, 1))]
    ]
    for disciplina in self.__disciplinas:
      layout.append([sg.Text(disciplina, size=(20, 1))])

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela disciplina').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__disciplinas = []
    return int(num['opcao'])

  def opcoes_disciplina(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Excluir disciplina', size=(15, 1))],
      [sg.Text('2 - Editar disciplina', size=(20, 1))],
      [sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Escolher operação').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    return int(num['opcao'])

  def opcoes_editar(self):
    layout = [
      [sg.Text('O que deseja editar:')],
      [sg.Text('1 - Nome', size=(15, 1))],
      [sg.Text('2 - Limite de alunos', size=(15, 1))],
      [sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Escolher edição').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    return int(num['opcao'])
  
  def novo_campo(self, indicador):
    if (indicador == 1):
      layout = [
        [sg.Text('Qual o novo nome:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Novo nome').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']
    else: 
      layout = [
        [sg.Text('Qual o novo limite:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Novo limite').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']

  def lista_disciplina(self, dados_disciplina):
    self.__disciplinas.append(dados_disciplina["opcao"])

  def lista_atividades(self, atividades):
    self.close()
    layout = [
      [sg.Text('Lista de atividades:', size=(20, 1))]
    ]
    for atividade in atividades:
      layout.append([sg.Text(atividade, size=(20, 1))])

    layout.append([sg.Cancel()])

    self.__window = sg.Window('Tela atividades').Layout(layout)
    self.__window.Close()
    self.open()
  
  def close(self): 
    self.__window.Close()