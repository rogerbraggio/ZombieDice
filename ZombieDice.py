import time
import random

aluno = 'Roger Eduardo Pompeu Braggio'
curso = 'Análise e Desenvolvimento de Sistemas'
print('\nAluno: {}\nCurso: {}\n'.format(aluno, curso))


def dado_verde():
    # função para criar o dado verde
    verde = ('C', 'P', 'C', 'T', 'P', 'C')
    return verde


def dado_amarelo():
    # função para criar o dado amarelo
    amarelo = ('T', 'P', 'C', 'T', 'P', 'C')
    return amarelo


def dado_vermelho():
    # função para criar o dado vermelho
    vermelho = ('T', 'P', 'T', 'C', 'P', 'T')
    return vermelho


def sortear_dados(cor_dado=()):
    # função para sortear os dados

    for j in range(0, 3):   # 'for' de 0 a 3 para sortear 3 dados

        num_sorteado = random.randint(0, 12)
        sorteado = lista_de_dados[num_sorteado]

        if sorteado == dado_verde():
            cor_dado = '\033[32mVERDE\033[m'
            # se sortear o dado verde 'cor_dado' recebe VERDE

        elif sorteado == dado_amarelo():
            cor_dado = '\033[33mAMARELO\033[m'
            # se sortear o dado amarelo 'cor_dado' recebe AMARELO

        elif sorteado == dado_vermelho():
            cor_dado = '\033[31mVERMELHO\033[m'
            # se sortear o dado vermelho 'cor_dado' recebe VERMELHO

        print('{}º dado sorteado: {}'.format(j+1, cor_dado))
        # printa o número do dado sorteado e em seguida a cor do dado sorteado

        dados_sorteados.append(sorteado)
        # insere os dados sorteados na lista 'dados_sorteados'


print('\033[1;31;107m=\033[m'*69)
print('\033[1;31;107m======================= Z O M B I E   D I C E =======================\033[m')
print('\033[1;31;107m=\033[m'*69, '\n')

qtd_jogadores = 0

while qtd_jogadores < 2:
    # enquanto a quantidade de jogadores for menor que 2 ele executará o código abaixo

    try:

        qtd_jogadores = int(input('Insira a quantidade de jogadores: '))

    except (ValueError, TypeError):

        # se o jogador inserir algo que não seja um número esse aviso irá aparecer
        print('\033[30;41mERRO!!! Por favor digite um número inteiro válido!\033[m')
        print('=-' * 25, '\n')
        continue

    if qtd_jogadores < 2:

        # se o jogador inserir um número inteiro menor que 2 esse aviso irá aparecer
        print('\033[30;41mQuantidade insuficiente de jogadores. No minímo 2!\033[m')
        print('=-'*25, '\n')

    elif qtd_jogadores >= 2:

        # essa parte coloquei somente para adicionar um espaço vazio
        print()
        break

lista_jogadores = []
# lista de jogadores começa vazia

for i in range(qtd_jogadores):
    # 'for' que vai rodar conforme a quantidade de jogadores

    nome_jogadores = str(input(f'Insira o nome do jogador nº {i+1}: '))
    # usuário insere o nome dos jogadores

    lista_jogadores.append(nome_jogadores)
    # o nome dos jogadores é adiciona a lista de jogadores

# lista contendo todos os dados
lista_de_dados = [dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(),
                  dado_amarelo(), dado_amarelo(), dado_amarelo(), dado_amarelo(),
                  dado_vermelho(), dado_vermelho(), dado_vermelho()]

jogador_atual = 0
tiro = 0
cerebro = 0
passo = 0
dados_sorteados = []
pontos = []

for i in range(qtd_jogadores):
    # função para adicionar pontuações conforme o número de jogadores

    pontos.append(0)
    # pontos serão adicionados para cada jogador

time.sleep(0.3)

print()

for i in range(len(lista_jogadores)):
    # função para mostrar os jogadores
    # i+1 para mostrar o número do jogador
    # lista_jogadores[i] para mostrar o nome do jogador

    print('Jogador {}: {}'.format(i+1, lista_jogadores[i]))

print()

time.sleep(0.6)
print('='*10, 'INICIANDO O JOGO!!!', '='*10, '\n')

while True:

    # o código abaixo vai executar até que um jogador acumule 13 pontos

    print('TURNO DE: {}'.format(lista_jogadores[jogador_atual]))
    # irá printar o turno do jogador atual

    print('\033[7mSORTEANDO OS DADOS\033[m', end='')

    # essa parte de código abaixo irá printar reticências temporizadas
    ret = 0
    while ret < 3:
        time.sleep(0.7)
        print('\033[7m.\033[m', end='')
        ret += 1

    print('\n')

    sortear_dados(cor_dado=())
    # chama a função sortear dados

    print()

    for dado_sorteado in dados_sorteados:

        face = random.randint(0, 5)
        # face vai receber um número de 0 a 5

        if dado_sorteado[face] == 'C':
            # o número sorteado vai escolher uma face do dado sorteado
            print('Face sorteada: CÉREBRO (você comeu um cérebro)')
            cerebro += 1

        elif dado_sorteado[face] == 'P':
            # o número sorteado vai escolher uma face do dado sorteado
            print('Face sorteada: PASSO (uma vítima fugiu)')
            passo += 1

        else:
            print('Face sorteada: TIRO (você tomou um tiro)')
            tiro += 1

    print('\n\033[7mPONTUAÇÃO:\033[m\nTIROS: {}\nCÉREBROS: {}\nPASSOS: {}'.format(tiro, cerebro, passo))
    # irá printar a quantidade de tiros, cérebros e passos que o jogador tirou

    if pontos[jogador_atual] + cerebro >= 13:
        # se o jogador acumular 13 cérebros o jogo irá encerrar

        print()

        # o código abaixo irá printar uma espécie de barra de loading
        ret = 0
        while ret < 25:
            time.sleep(0.07)
            print('\033[7m.\033[m', end='')
            ret += 1

        time.sleep(0.5)
        print()
        print('\nPARABÉNS {}, VOCÊ COMEU {} CÉREBROS!!!'
              .format(lista_jogadores[jogador_atual], (pontos[jogador_atual] + cerebro)))
        # irá mostrar quem foi o jogador vencedor e a quantidade de cérebros que ele comeu
        print('\nFIM DO JOGO!')
        break

    if tiro > 2:
        # se o jogador tirar 3 tiros no turno seu turno se encerrará e ele não irá acumular os cérebros da rodada

        print('\033[30;41mVOCÊ PERDEU OS PONTOS ACUMULADOS NESSA RODADA! Levou {} tiros\033[m'.format(tiro))
        tiro = 0  # zera os tiros
        cerebro = 0  # zera os cérebros
        passo = 0  # zera os passos
        dados_sorteados = []  # limpa a lista de dados sorteados
        jogador_atual += 1  # passa para o próximo jogador

        if jogador_atual == len(lista_jogadores):
            # se o jogador que está jogando for o último da lista, 'jogador_atual' irá receber 0 para voltar para
            # o primeiro jogador da lista
            jogador_atual = 0

    else:
        # se o jogador não tirar 3 tiros ele poderá escolher entre continuar ou parar seu turno

        continuar_turno = str(input('\nVocê deseja continuar seu turno [s = sim / n = não]? '))
        print()

        if continuar_turno == 'n' or continuar_turno == 'N' or continuar_turno == 'nao':
            # se o jogador escolher não continuar:

            pontos[jogador_atual] += cerebro  # os cérebros serão contabilizados no placar total
            jogador_atual += 1  # passará o turno para o próximo jogador
            dados_sorteados = []  # vai limpar a lista de dados sorteados
            cerebro = 0  # cérebros irão zerar
            tiro = 0  # tiros irão zerar
            passo = 0  # passos irão zerar

            if jogador_atual == len(lista_jogadores):
                # se o jogador que está jogando for o último da lista, 'jogador_atual' irá receber 0 para voltar para
                # o primeiro jogador da lista
                jogador_atual = 0

    print('\033[30;42m .::::. P L A C A R .::::. \033[m')

    for i in range(qtd_jogadores):
        # vai printar um placar com os nomes dos jogadores e suas respectivas pontuações (cérebros comidos)

        print('Pontos de {}: {} pontos'.format(lista_jogadores[i], pontos[i]))
        pass

    dados_sorteados.clear()
    # limpa a lista de dados sorteados

    print()
    print('-'*100)
    print()
