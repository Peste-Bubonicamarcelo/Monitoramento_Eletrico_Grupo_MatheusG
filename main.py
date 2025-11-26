import dados
import function


#Arquivo menu que chama as funções e os dados
def main():
    opc = "0"
    while opc != "6":
        if opc == "0":
            print("=== Sistema de Monitoramento Elétrico ===")
            print("1 - Registrar medição")
            print("2 - Salvar circuitos")
            print("3 - Gerar relatório de não conformidade")
            print("4 - Resumo elétrico")
            print("5 - Rodar módulo extra")
            print("6 - Sair")
            opc = input("Escolha: ")
        elif opc == "1":
            linha = input("Digite: Nome; V=...; I=...; fp=...; f=...\n")
            function.registrar_medicao(linha)
            opc = "0"
        elif opc == "2":
            # Alterado para usuário escolher o nome
            nome_arq = input("Digite o nome do arquivo").strip().lower()
            function.salvar_circuitos(nome_arq)
            opc = "0"
        elif opc == "3":
            function.gerar_relatorio_nao_conforme()
            opc = "0"
        elif opc == "4":
            function.resumo_eletrico()
            opc = "0"
        elif opc == "5":
            function.mod_extra()
            opc = "0"
        else:
            print("Opção inválida")

main()
#das;v=3;i=3;fp=3;f=4