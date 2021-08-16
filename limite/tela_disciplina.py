class TelaAluno():
  def tela_opcoes(self):
    print("-------- DISCIPLINA ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar disciplina")
    print("2 - Listar disciplinas")
    print("3 - Listar atividades")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

 def pega_dados_disciplina(self):
    print("-------- DADOS DISCIPLINA ----------")
    nome = input("Nome: ")
    limite_alunos = input("Limite alunos: ")
    return {"nome": nome, "limite_alunos": limite_alunos}

  def pega_nome_disciplina(self):
    print("-------- NOME DISCIPLINA ----------")
    nome = input("Nome: ")
    return nome
