class TelaSistema:
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- SisLivros ---------")
        print("Escolha sua opcao")
        print("1 - Curso")
        print("2 - Professor")
        print("3 - Disciplina")
        print("4 - Aluno")
        print("5 - Atividade")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao
