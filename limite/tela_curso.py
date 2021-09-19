class TelaCurso():
  def tela_opcoes(self):
    print("-------- CURSO ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar Curso")
    print("2 - Operações do curso")
    print("3 - Relatórios do curso")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_curso(self):
    print("-------- DADOS CURSO ----------")
    nome = input("Nome: ")
    instituicao = input("Instituição: ")
    return {"nome": nome, "instituicao": instituicao}

  def mostra_curso(self, dados_curso):
    print("NOME DO CURSO: ", dados_curso["nome"])
    print("INSTITUIÇÃO: ", dados_curso["instituicao"])
    print("\n")

  def seleciona_curso(self):
    print("-------- QUAL CURSO? ----------")
    curso = int(input("Curso: "))
    return curso

  def opcoes_curso(self):
    print("-------- O QUE DESEJA FAZER? ----------")
    print("1 - Excluir")
    print("2 - Editar")
    opcao = int(input("Escolha a opção: "))
    return opcao

  def opcoes_editar(self):
    print("-------- O QUE DESEJA EDITAR? ----------")
    print("1 - Nome")
    print("2 - Instituição")
    opcao = int(input("Escolha a opção: "))
    return opcao
  
  def novo_campo(self):
    print("-------- NOVO VALOR ----------")
    opcao = input("Qual o novo valor?: ")
    return opcao

  def lista_curso(self, dados_curso):
    print(dados_curso["opcao"])
