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

  def pega_dados_atividade(self, oi):
    print("-------- DADOS CURSO ----------")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prazo = input("Prazo: ")

    return {"titulo": titulo, "descricao": descricao, "prazo": prazo, "disciplina": disciplina}

  def mostra_atividade(self, dados_atividade):
    print("TÍTULO: ", dados_atividade["titulo"])
    print("DESCRIÇÃO: ", dados_atividade["descricao"])
    print("PRAZO: ", dados_atividade["prazo"])
    if dados_atividade["entregue"]:
        print("DATA DE ENTREGA: ", dados_atividade["data_entregue"])
        print("NOTA: ", dados_atividade["nota"])
    print("\n")

  def lista_atividade(self, dados_atividade):
    print(dados_atividade["opcao"])

  def seleciona_atividade(self):
    atividade = int(input("Atividade: "))
    return atividade

  def opcoes_atividade(self):
    print("-------- ATIVIDADE ----------")
    print("Escolha a opcao")
    print("1 - Excluir")
    print("2 - Entregar")
    print("3 - Corrigir")
    opcao = int(input("Escolha a opcao: "))
    return opcao

  def corrigir(self):
    nota = int(input("Dê uma nota: "))
    return nota

