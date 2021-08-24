class TelaDisciplina():
  def tela_opcoes(self):
    print("-------- DISCIPLINA ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar disciplina")
    print("2 - Operações da disciplina")
    print("3 - Listar atividades")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao
    
  def pega_dados_disciplina(self):
    print("-------- DADOS DISCIPLINA ----------")
    nome = input("Nome: ")
    limite_alunos = input("Limite de alunos: ")
    return {"nome": nome, "limite_alunos": limite_alunos}

  def pega_nome_disciplina(self):
    print("-------- NOME DISCIPLINA ----------")
    nome = input("Nome: ")
    return nome

  def seleciona_disciplina(self):
    print("-------- QUAL DISCIPLINA? ----------")
    disciplina = int(input("disciplina: "))
    return disciplina

  def opcoes_disciplina(self):
    print("-------- O QUE DESEJA FAZER? ----------")
    print("1 - Excluir")
    print("2 - Editar")
    opcao = int(input("Escolha a opção: "))
    return opcao

  def opcoes_editar(self):
    print("-------- O QUE DESEJA EDITAR? ----------")
    print("1 - Nome")
    print("2 - Limite de alunos")
    opcao = int(input("Escolha a opção: "))
    return opcao
  
  def novo_campo(self, indicador):
    print("-------- NOVO VALOR ----------")
    if (indicador == 1):
      opcao = int(input("Qual a novo limite de alunos?: "))
    elif (indicador == 2):
      opcao = input("Qual o novo nome?: ")
    return opcao

  def lista_disciplina(self, dados_disciplina):
    print(dados_disciplina["opcao"])