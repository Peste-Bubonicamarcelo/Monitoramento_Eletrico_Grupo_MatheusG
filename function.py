import dados

def dentro_da_faixa(circuito):
    nome, tipo, v, i, fp, f, data = circuito
    regra = dados.limites.get(tipo, None)
    if not regra:
        return True
    if not (regra["tensao_nom"] * (1 - dados.tolerancia_tensao) <= v <= regra["tensao_nom"] * (1 + dados.tolerancia_tensao)):
        return False
    if i > regra["i_max"]:
        return False
    if fp < regra["fp_min"]:
        return False
    return True

def registrar_medicao(linha):
    partes = linha.split(";")
    nome = partes[0].strip()
    medidas = {}
    for pedaco in partes[1:]:
        pedaco = pedaco.strip()
        if "=" in pedaco:
            k, v = pedaco.split("=")
            medidas[k.strip().lower()] = v.strip()

    for c in dados.circuitos:
        if c[0] == nome:
            if "v" in medidas:
                c[2] = float(medidas["v"])
            if "i" in medidas:
                c[3] = float(medidas["i"])
            if "fp" in medidas:
                c[4] = float(medidas["fp"])
            if "f" in medidas:
                c[5] = float(medidas["f"])
            break

def salvar_circuitos(nome_arquivo):
    with open(nome_arquivo, "w") as arq:
        for c in dados.circuitos:
            linha = f"{c[0]};{c[1]};{c[2]};{c[3]};{c[4]};{c[5]};{c[6]}\n"
            arq.write(linha)
    print("Circuitos salvos em", nome_arquivo)

def gerar_relatorio_nao_conforme(nome_arquivo="relatorio_nao_conforme.txt"):
    with open(nome_arquivo, "w") as arq:
        arq.write("RELATÓRIO DE NÃO CONFORMIDADE\n\n")
        for c in dados.circuitos:
            if not dentro_da_faixa(c):
                arq.write(f"Circuito: {c[0]}\n")
                arq.write(f"  Tipo: {c[1]} | V={c[2]} V | I={c[3]} A | fp={c[4]} | f={c[5]} Hz\n\n")
    print("Relatório gerado.")

def resumo_eletrico():
    menor_fp = min(dados.circuitos, key=lambda x: x[4])
    fora = [c for c in dados.circuitos if not dentro_da_faixa(c)]
    print("Circuito com menor fator de potência:", menor_fp[0], "-", menor_fp[4])
    print("Total de circuitos fora da faixa:", len(fora))

def gmod_extra():
    tin = 0
    tout = 0
    ups=False
    while True:
        print("==~Monitoramento UPS~==")
        print("1 - Adicionar Valor de circuito")
        print("2 - Sair")
        comand = input()
        if comand == "1":
            inp = float(input("Valor de entrada:"))
            out = float(input("Valor de saída:"))
            tin= inp
            tout= out
            break
        elif comand == "2":
            break
        else:
            print("Digite um valor valido.")

    if tin<200:
        ups=True
        print("UPS acionada")
    with open("registro.txt","w") as arq:
        arq.write("===~Registro de medições~===\n\n")
        arq.write("Valor de entrada: ")
        arq.write(str(tin))
        arq.write("V\n")
        arq.write("Valor de saída: ")
        arq.write(str(tout))
        arq.write("V\n")
        if ups==True:
            arq.write("Ups acionada")
        else:
            arq.write("Ups não acionada")