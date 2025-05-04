linha = 1
coluna = 1

while linha <= 10:
    while coluna < 10:
        coluna = coluna + 1
        print(linha," x ",coluna,"=",(coluna*linha),end ="\t")
    linha = linha + 1
    print ()
    coluna = 1
