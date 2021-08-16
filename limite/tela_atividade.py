class TelaAtividade():
  def tela_opcoes(self):
    print("-------- ATIVIDADE ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar Atividade")
    print("2 - Visualizar Atividades")
    print("3 - Operar Atividade")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_atividade(self):
    print("-------- DADOS CURSO ----------")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prazo = input("Prazo: ")

    return {"titulo": titulo, "descricao": descricao, "prazo": prazo}

  def mostra_atividade(self, dados_atividade):
    print("NOME DO CURSO: ", dados_atividade["nome"])
    print("\n")
