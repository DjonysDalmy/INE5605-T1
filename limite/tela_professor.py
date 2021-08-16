class TelaProfessor():
  def tela_opcoes(self):
    print("-------- PROFESSOR ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar professor")
    print("2 - Cadastrar atividade")
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