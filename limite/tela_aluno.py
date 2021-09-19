import PySimpleGUI as sg

class TelaAluno():
  def __init__(self): 
    self.__window = None
    self.__alunos = []

  def init_components(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Cadastrar Aluno', size=(15, 1))],
      [sg.Text('2 - Operações do Aluno', size=(20, 1))],
      [sg.Text('3 - Listar disciplinas', size=(20, 1))],
      [sg.Text('4 - Listar atividades', size=(20, 1))],
      [sg.Text('0 - Voltar', size=(20, 1))],
      [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Tela aluno').Layout(layout)

  def open(self):
    self.init_components()
    values = self.__window.Read()
    return values

  def pega_dados_aluno(self):
    self.close()
    layout = [
      [sg.Text('Escolha os dados do aluno:')],
      [sg.Text('Nome do aluno:', size=(15, 1)), sg.InputText("", key="nome")],
      [sg.Text('Idade do aluno:', size=(15, 1)), sg.InputText("", key="idade")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Adicionar aluno').Layout(layout)
    values = self.__window.Read()
    self.__window.Close()
    return values[1]
  
  def seleciona_aluno(self):
    self.close()
    layout = [
      [sg.Text('Escolha o aluno:', size=(20, 1))]
    ]
    for aluno in self.__alunos:
      layout.append([sg.Text(aluno, size=(20, 1))])

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela aluno').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__alunos = []
    return int(num['opcao'])

  def opcoes_aluno(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Excluir aluno', size=(15, 1))],
      [sg.Text('2 - Editar aluno', size=(20, 1))],
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

  def lista_aluno(self, dados_aluno):
    self.__alunos.append(dados_aluno["opcao"])

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

  def lista_disciplinas(self, disciplinas):
    self.close()
    layout = [
      [sg.Text('Lista de disciplinas:', size=(20, 1))]
    ]
    for disciplina in disciplinas:
      layout.append([sg.Text(disciplina, size=(20, 1))])

    layout.append([sg.Cancel()])

    self.__window = sg.Window('Tela disciplinas').Layout(layout)
    self.open()

  def pega_nome_aluno(self):
    self.close()
    layout = [
      [sg.Text('Qual o nome do aluno:', size=(20, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Qual o nome').Layout(layout)
    values = self.__window.Read()
    valor = values[1]
    self.__window.Close()
    return valor['opcao']
  
  def close(self): 
    self.__window.Close()