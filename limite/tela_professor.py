import PySimpleGUI as sg

class TelaProfessor():
  def __init__(self): 
    self.__window = None
    self.__professores = []

  def init_components(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Cadastrar Professor', size=(20, 1))],
      [sg.Text('2 - Operações do Professor', size=(20, 1))],
      [sg.Text('3 - Listar disciplinas', size=(20, 1))],
      [sg.Text('4 - Vincular disciplina', size=(20, 1))],
      [sg.Text('0 - Voltar', size=(20, 1))],
      [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Tela professor').Layout(layout)

  def open(self):
    self.init_components()
    values = self.__window.Read()
    return values

  def pega_dados_professor(self):
    self.close()
    layout = [
      [sg.Text('Escolha os dados do professor:')],
      [sg.Text('Nome do professor:', size=(15, 1)), sg.InputText("", key="nome")],
      [sg.Text('Idade do professor:', size=(15, 1)), sg.InputText("", key="idade")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Adicionar professor').Layout(layout)
    values = self.__window.Read()
    self.__window.Close()
    return values[1]
  
  def seleciona_professor(self):
    self.close()
    layout = [
      [sg.Text('Escolha o professor:', size=(20, 1))]
    ]
    for professor in self.__professores:
      layout.append([sg.Text(professor, size=(20, 1))])

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela professor').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__professores = []
    return int(num['opcao'])

  def opcoes_professor(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Excluir professor', size=(15, 1))],
      [sg.Text('2 - Editar professor', size=(20, 1))],
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
      [sg.Text('2 - Idade', size=(15, 1))],
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
        [sg.Text('Qual a nova idade:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Nova idade').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']
    else: 
      layout = [
        [sg.Text('Qual o novo nome:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Novo nome').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']

  def lista_professor(self, dados_professor):
    self.__professores.append(dados_professor["opcao"])

  def lista_disciplinas(self, disciplinas):
    self.close()
    layout = [
      [sg.Text('Lista de disciplinas:', size=(20, 1))]
    ]
    for disciplina in disciplinas:
      layout.append([sg.Text(disciplina, size=(20, 1))])

    layout.append([sg.Cancel()])

    self.__window = sg.Window('Tela disciplinas').Layout(layout)
    self.__window.Close()
    self.open()

  def vincular_disciplina(self, disciplinas): 
    self.close()
    layout = [
      [sg.Text('Escolha a disciplina:', size=(20, 1))]
    ]
    for disciplina in disciplinas:
      layout.append([sg.Text(disciplina, size=(20, 1))])

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela disciplina').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__professores = []
    return int(num['opcao'])

  def pega_nome_professor(self):
    self.close()
    layout = [
      [sg.Text('Qual o nome do professor:', size=(20, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Qual o nome').Layout(layout)
    values = self.__window.Read()
    valor = values[1]
    self.__window.Close()
    return valor['opcao']
  
  def close(self): 
    self.__window.Close()