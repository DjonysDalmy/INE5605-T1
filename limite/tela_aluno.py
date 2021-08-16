class TelaAluno():
  def tela_opcoes(self):
    print("-------- ALUNO ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar aluno")
    print("2 - Enviar atividade")
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
