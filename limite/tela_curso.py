import PySimpleGUI as sg

class TelaCurso():
  def __init__(self): 
      self.__window = None
      self.__cursos = []

  def init_components(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Cadastrar Curso', size=(15, 1))],
      [sg.Text('2 - Operações do curso', size=(20, 1))],
      [sg.Text('3 - Relatórios do curso', size=(20, 1))],
      [sg.Text('0 - Voltar', size=(20, 1))],
      [sg.Text('Escolha o desejado:', size=(15, 1)), sg.InputText()],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Tela curso').Layout(layout)

  def open(self):
    self.init_components()
    values = self.__window.Read()
    return values

  def pega_dados_curso(self):
    self.close()
    layout = [
      [sg.Text('Escolha o nome do curso:')],
      [sg.Text('Nome do curso:', size=(15, 1)), sg.InputText("", key="nome")],
      [sg.Text('Nome da instituição: ', size=(15, 1)), sg.InputText("", key="instituicao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Criar curso').Layout(layout)
    values = self.__window.Read()
    self.__window.Close()
    return values[1]

  def seleciona_curso(self, cursos):
    self.close()
    layout = [
      [sg.Text('Escolha o curso:', size=(20, 1))]
    ]
    i = 0
    for curso in cursos:
      layout.append([sg.Text(str(i) + ": " + curso.nome, size=(20, 1))])
      i +=1

    layout.extend([[sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")], [sg.Submit()]])

    self.__window = sg.Window('Tela curso').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    self.__cursos = []
    return int(num['opcao'])

  def relatorio_curso(self, cursos):
    self.close()
    layout = [
      [sg.Text('Lista de cursos:', size=(20, 1))]
    ]
    for curso in cursos:
      layout.append([sg.Text("Curso: " + curso.nome, size=(20, 1))])
      layout.append([sg.Text("Instituição: " + curso.instituicao, size=(20, 1))])
      layout.append([sg.Text("---", size=(20, 1))])

    self.__window = sg.Window('Tela relatórios').Layout(layout)
    self.__cursos = []
    values = self.__window.Read()
    num = values[0]
    self.__window.Close()
    return num

  def opcoes_curso(self):
    layout = [
      [sg.Text('Escolha sua opção:')],
      [sg.Text('1 - Excluir curso', size=(15, 1))],
      [sg.Text('2 - Editar curso', size=(20, 1))],
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
      [sg.Text('2 - Instituição', size=(15, 1))],
      [sg.Text('Qual opção:', size=(15, 1)), sg.InputText(key="opcao")],
      [sg.Submit()]
    ]
    self.__window = sg.Window('Escolher edição').Layout(layout)
    values = self.__window.Read()
    num = values[1]
    self.__window.Close()
    return int(num['opcao'])
  
  def novo_campo(self, opcao):
    if (opcao == 1): 
      layout = [
        [sg.Text('Qual o novo nome:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Novo nome').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']
    if (opcao == 2): 
      layout = [
        [sg.Text('Qual a nova instituição:', size=(15, 1)), sg.InputText(key="opcao")],
        [sg.Submit()]
      ]
      self.__window = sg.Window('Nova instituição').Layout(layout)
      values = self.__window.Read()
      valor = values[1]
      self.__window.Close()
      return valor['opcao']

  def lista_curso(self, dados_curso):
    self.__cursos.append(dados_curso["opcao"])
  
  def close(self): 
    self.__window.Close()