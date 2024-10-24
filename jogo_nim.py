# Função para a jogada do computador
def computador_escolhe_jogada(n, m):
    # O computador vai tentar deixar múltiplos de (m+1) para o jogador
    for i in range(1, m+1):
        if (n - i) % (m + 1) == 0:
            return i
    # Se não puder, remove o máximo possível
    return min(n, m)

# Função para a jogada do usuário
def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")

# Função para uma partida isolada
def partida():
    # Solicita o número de peças e o limite por jogada
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    # Decide quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_computador = False
    else:
        print("Computador começa!")
        vez_do_computador = True

    # Enquanto ainda houver peças no tabuleiro
    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça{'s' if jogada > 1 else ''}.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça{'s' if jogada > 1 else ''}.")
        
        n -= jogada
        if n > 0:
            print(f"Agora restam {n} peças no tabuleiro.\n")
        vez_do_computador = not vez_do_computador
    
    # Fim do jogo
    if vez_do_computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

# Função para o campeonato (3 partidas)
def campeonato():
    print("Você escolheu um campeonato!")
    placar_usuario = 0
    placar_computador = 3
    
    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****\n")
        partida()
    
    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")

# Função principal que define o início do jogo
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input())
    
    if escolha == 1:
        print("Você escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        campeonato()

# Executa o programa principal
main()