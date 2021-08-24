class TelaAluno():
  def tela_opcoes(self):
    print("-------- ALUNO ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar aluno")
    print("2 - Operações do aluno")
    print("3 - Listar disciplinas")
    print("4 - Listar atividades")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_aluno(self):
    print("-------- DADOS ALUNO ----------")
    nome = input("Nome: ")
    idade = input("Idade: ")
    return {"nome": nome, "idade": idade}

  def pega_nome_aluno(self):
    print("-------- NOME ALUNO ----------")
    nome = input("Nome: ")
    return nome

  def seleciona_aluno(self):
    print("-------- QUAL ALUNO? ----------")
    aluno = int(input("Aluno: "))
    return aluno

  def opcoes_aluno(self):
    print("-------- O QUE DESEJA FAZER? ----------")
    print("1 - Excluir")
    print("2 - Editar")
    opcao = int(input("Escolha a opção: "))
    return opcao

  def opcoes_editar(self):
    print("-------- O QUE DESEJA EDITAR? ----------")
    print("1 - Nome")
    print("2 - Idade")
    opcao = int(input("Escolha a opção: "))
    return opcao
  
  def novo_campo(self, indicador):
    print("-------- NOVO VALOR ----------")
    if (indicador == 1):
      opcao = int(input("Qual a nova idade?: "))
    elif (indicador == 2):
      opcao = input("Qual o novo nome?: ")
    return opcao

  def lista_aluno(self, dados_aluno):
    print(dados_aluno["opcao"])