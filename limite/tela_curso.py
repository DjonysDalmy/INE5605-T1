class TelaCurso():
  def tela_opcoes(self):
    print("-------- CURSO ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar Curso")
    print("2 - Relatório do curso")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_curso(self):
    print("-------- DADOS CURSO ----------")
    nome = input("Nome: ")

    return {"nome": nome}

  def mostra_curso(self, dados_curso):
    print("NOME DO CURSO: ", dados_curso["nome"])
    print("\n")
