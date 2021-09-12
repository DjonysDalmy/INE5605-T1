class TelaProfessor():
  def tela_opcoes(self):
    print("-------- PROFESSOR ----------")
    print("Escolha a opcao: ")
    print("1 - Cadastrar professor")
    print("2 - Operações do professor")
    print("3 - Listar disciplinas")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_professor(self):
    print("-------- DADOS PROFESSOR ----------")
    nome = input("Nome: ")
    idade = input("Idade: ")
    return {"nome": nome, "idade": idade}

  def pega_nome_professor(self):    
    print("-------- NOME PROFESSOR ----------")
    nome = input("Nome: ")
    return nome
  
  def seleciona_professor(self):
    print("-------- QUAL PROFESSOR? ----------")
    professor = int(input("Professor: "))
    return professor

  def opcoes_professor(self):
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

  def lista_professor(self, dados_professor):
    print(dados_professor["opcao"])