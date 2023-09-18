"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# ======================================================================
#
#   M Ó D U L O pacman
#   
#   Módulo responsável por todo o controle do jogo. Várias funções só
#   possuem os protótipos escritos aqui. Você deverá finalizá-las.
#
#   Não altere o nome do arquivo
#   
#   Não importe outros módulos além do random e do sys e
#   eventualmente o  extras
#
#   Não altere funções que possuem nos seus comentários: 
#   !!!NÃO MODIFIQUE ESTA FUNÇÃO!!!
#
# ======================================================================

# módulo para sorteio de números pseudo aleatórios
import random

# Se você criou funções adicionais e colocou em extras.py,
# descomente a linha abaixo
#import extras

# módulo para permitir a saída do programa caso haja erro na abertura
# do arquivo
import sys

# CONSTANTES
ESQUERDA = 0   # 'a'
DIREITA  = 1   # 's'
CIMA     = 2   # 'w'
BAIXO    = 3   # 'z'
PARADO   = 4

PACMAN   = 'C'
FANTASMA = 'F'
VAZIO    = ' '
PACDOT   = '.'
PAREDE   = '+'

semente=0
random.seed(semente)
# ======================================================================

def leLabirinto(nomeDoArquivo):
    ''' (string) -> matriz

    !!!NÃO MODIFIQUE ESTA FUNÇÃO!!!
   
    Recebe uma string com o nome de um arquivo texto que
    contém uma configuração inicial do jogo. Na configuração inicial

       '+' representa uma parede;
       '.' representa um pac-dot;
       'C' representa o Pac-Man;
       'F' representa um fantasma

    A função processa este arquivo e devolve como saída uma matriz de
    caracteres com um caractere em cada posição da matriz

    !!!NÃO MODIFIQUE ESTA FUNÇÃO!!!
    '''
   
    # Abrimos o arquivo. Se isso nao for possivel, imprime-se uma
    # mensagem de erro e o programa e' terminado.
    try:
        arquivo = open(nomeDoArquivo, 'r')
    except:
        print("Nao consegui abrir o arquivo %s" % nomeDoArquivo)
        sys.exit(0)

    # Lemos ate a primeira linha vazia.
    linhas = [ ]
    for linha in arquivo:
        s = linha.rstrip()   # remove caracteres de fim de linha do arquivo

        if s:
            linhas.append(s)
        else:
            break

    # Se o labirinto e' vazio, entao imprime-se uma mensagem de erro e
    # o programa e' terminado.
    if not linhas:
        print('O labirinto nao pode ser vazio')
        sys.exit(0)

    # Cria-se a matriz com o labirinto. Se as linhas nao tem todas o
    # mesmo tamanho, o programa e' encerrado. Se o pacman nao for
    # encontrado, o programa e' encerrado.
    m, n = len(linhas), len(linhas[0])
    lab = [ ]
    encontrou_pacman = False

    for i in range(m):
        if len(linhas[i]) != n:
            print('As linhas devem ter todas o mesmo tamanho')
            sys.exit(0)

        linhalab = [ ]
        for j in range(n):
            if linhas[i][j] not in '+.CF':
                print('Caractere invalido encontrado')
                sys.exit(0)

            linhalab.append(linhas[i][j])

            if linhas[i][j] == 'C':
                if encontrou_pacman:
                    print('Pac-Man ja foi especificado')
                    sys.exit(0)
               
                encontrou_pacman = True

        lab.append(linhalab)

    if not encontrou_pacman:
        print('Pac-Man nao foi encontrado no labirinto')
        sys.exit(0)

    return lab


# ======================================================================

def criaPacMan(lab):
    ''' (matriz) -> [int, int, int, int]

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe uma matriz de caracteres representando a configuração inicial
    do labirinto e encontra o Pac-Man. No lugar do Pac-Man, na matriz,
    coloca um espaço vazio que representa a posição vazia. Retorna uma
    lista com as informações do Pac-Man:

           [linha, coluna, direção, pontos]

    Nada é impresso por essa função.

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''
    
    # escreva sua função a seguir
    pacman=[]
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j]=='C':
                lab[i][j]=' '
                pacman.append(i)
                pacman.append(j)
                pacman.append(4)
                pacman.append(0)
    return pacman

 

# ======================================================================

def criaFantasmas(lab):
    '''  (matriz) -> [[int, int, int], [int, int, int], ...]

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe uma matriz de caracteres representando a configuração
    inicial do labirinto e encontra os fantasmas. No lugar de cada
    fantasma, na matriz, coloca um '.' que representa um pac-dot.
    Devolve uma matriz (lista de lstas) com as informações dos fantasmas:

      [[linha, coluna, direção],
       [linha, coluna, direção],
       [linha, coluna, direção],
       ...]

    Nada é impresso por essa função.

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''
    
    # escreva sua função a seguir
    fantasmas=[]
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            c=False
            posfant=[]
            if lab[i][j]=='F':
                posfant.append(i)
                posfant.append(j)
                while not c:
                    d=random.randrange(0,4)
                    if (d==0 and lab[i][(j-1)%len(lab[0])]!='+') or (d==1 and lab[i][(j+1)%len(lab[0])]!='+') or (d==2 and lab[(i-1)%len(lab)][j]!='+') or (d==3 and lab[(i+1)%len(lab)][j]!='+'): 
                        posfant.append(d)
                        fantasmas.append(posfant)
                        c=True
                lab[i][j]='.'
    return fantasmas


# ======================================================================

def imprimeLabirinto(lab, pacman, fantasmas):
    ''' (matriz, lista, matriz) -> None

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe uma matriz de caracteres representando o labirinto, a lista
    representando o pacman e a matriz representando os fantasmas e
    imprime corretamente o labirinto sem devolver nada.

    Caso um fantasma esteja na mesma posição do Pac-man, deverá
    ser impresso na posição em questão o caractere especial 'X'.

    Senão, o Pac-Man, que não estará na matriz do labirinto, mas sim na
    sua própria lista, deve ser impresso como um C, e cada fantasma,
    que não estará na matriz do labirinto, mas sim na sua própria
    matriz, deve ser impresso como um F

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''
   
    # escreva sua função a seguir
    for i in range(len(lab)):
        s=''
        for j in range(len(lab[0])):
            FANT=False
            for k in range(len(fantasmas)):
                if fantasmas[k][0]==i and fantasmas[k][1]==j:
                    FANT=True
            if not FANT:
                if pacman[0]==i and pacman[1]==j:
                    s+='C'
                else: 
                    s+=lab[i][j]
            if FANT:
                if i==pacman[0] and j==pacman[1]:
                    s+='X'
                else: s+='F'
        print(s)
    

# ======================================================================
def movimentaFantasmas(lab, fantasmas):
    '''  (matriz, matriz) -> None

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe uma matriz de caracteres representando o labirinto e a
    matriz representando os fantasmas e, para cada fantasma, atualiza a
    sua posição levando em conta a informação de direção de cada um (que
    está armazenada na linha correspondente da matriz dos fantasmas).

    A matriz do labirinto não deve ser modificada. Apenas a matriz dos
    fantasmas deve ser modificada de acordo com a direção de movimentação
    de cada fantasma. Note que antes de mover o fantasma deve-se verificar
    se a direção pode continuar sendo a mesma. Caso seja necessário, ou
    possível, mudar a direção, uma nova direção deve ser sorteada.
 
    A função deve, ainda, imprimir para cada fantasma, as coordenadas
    da posição na qual ela se encontrava e a direção do movimento.

    Lembre que o labirinto é cíclico.

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''

    # escreva sua função a seguir
    for k in range(len(fantasmas)):
        l=fantasmas[k][0]
        c=fantasmas[k][1]
        if fantasmas [k][2]==0:
            print("Um fantasma moveu-se de (%d,%d) para (%d,%d)"%(l,c,l,(c-1)%len(lab[0])))
            c=fantasmas[k][1]=(fantasmas[k][1]-1)%len(lab[0])
        if fantasmas [k][2]==1:
            print("Um fantasma moveu-se de (%d,%d) para (%d,%d)"%(l,c,l,(c+1)%len(lab[0])))
            c=fantasmas[k][1]=(fantasmas[k][1]+1)%len(lab[0])
        if fantasmas [k][2]==2:
            print("Um fantasma moveu-se de (%d,%d) para (%d,%d)"%(l,c,(l-1)%len(lab),c))
            l=fantasmas[k][0]=(fantasmas[k][0]-1)%len(lab)
        if fantasmas [k][2]==3:
            print("Um fantasma moveu-se de (%d,%d) para (%d,%d)"%(l,c,(l+1)%len(lab),c))
            l=fantasmas[k][0]=(fantasmas[k][0]+1)%len(lab)
        d_possiveis=[]
        if lab[l][(c-1)%len(lab[0])]!='+':
            d_possiveis.append(0)
        if lab[l][(c+1)%len(lab[0])]!='+':
            d_possiveis.append(1)
        if lab[(l-1)%len(lab)][c]!='+':
            d_possiveis.append(2)
        if lab[(l+1)%len(lab)][c]!='+':
            d_possiveis.append(3)
        possivel=False
        nova_d=0
        while not possivel:
            nova_d=random.randrange(0,4)
            for x in d_possiveis:
                if x==nova_d:
                    possivel=True
            
        if len(d_possiveis)>2:
            fantasmas[k][2]=nova_d
        if len(d_possiveis)==2:
            if d_possiveis==[0,3] or d_possiveis==[0,2] or d_possiveis==[1,2] or d_possiveis==[1,3]:
                fantasmas[k][2]=nova_d
        if len(d_possiveis)==1:
            fantasmas[k][2]=d_possiveis[0]
        


# ======================================================================

def verificaColisao(pacman, fantasmas):
    '''  (lista, matriz) -> bool

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe uma lista com as informações do Pac-Man e a matriz
    representando os fantasmas e verifica se algum fantasma está na mesma
    posição do Pac-Man. Se algum fantasma está na mesma posição do
    Pac-Man, retorna True. Se nenhum fantasma está na mesma posição do
    Pac-Man, retorna False. Nada é impresso por essa função.
    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''

    # escreva sua função a seguir
    choque=False
    for i in range(len(fantasmas)):
        if fantasmas[i][0]==pacman[0] and fantasmas[i][1]==pacman[1]:
            choque=True
    return choque




# ======================================================================

def movimentaPacMan(lab, pacman):
    ''' (matriz, lista) -> None

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe a matriz de caracteres representando o labirinto e a lista
    representando o Pac-Man e tenta movimentar o Pac-Man na direção
    armazenada na sua lista. Se for possível movimentar, faz isso
    modificando as informações de localização na lista do Pac-Man. Se
    não for possível movimentar, porque há uma parede na direção, nada
    muda na lista do Pac-Man.

    IMPORTANTE: toda a verificação de se há fantasma ou pac-dot na nova
    posição NÃO deve ser feita aqui mas sim no main. 

    A função deve, ainda, imprimir as coordenadas da posição antes
    e depois, caso tenha havido movimento.

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''

    # escreva sua função a seguir
    if pacman[2]==0:
        if lab[pacman[0]][(pacman[1]-1)%len(lab[0])]!='+':
            pacman[1]=(pacman[1]-1)%len(lab[0])
            print("Pac-man moveu-se de (%d,%d) para (%d,%d)"%(pacman[0], (pacman[1]+1)%len(lab[0]), pacman[0], pacman[1]))
        if lab[pacman[0]][(pacman[1]-1)%len(lab[0])]=='+':
            print("movimento do Pac-Man não é possível.")

    if pacman[2]==1:
        if lab[pacman[0]][(pacman[1]+1)%len(lab[0])]!='+':
            pacman[1]=(pacman[1]+1)%len(lab[0])
            print("Pac-man moveu-se de (%d,%d) para (%d,%d)"%(pacman[0], (pacman[1]-1)%len(lab[0]), pacman[0], pacman[1]))
        if lab[pacman[0]][(pacman[1]+1)%len(lab[0])]=='+':
            print("movimento do Pac-Man não é possível.")

    if pacman[2]==2:
        if lab[(pacman[0]-1)%len(lab)][pacman[1]]!='+':
            pacman[0]=(pacman[0]-1)%len(lab)
            print("Pac-man moveu-se de (%d,%d) para (%d,%d)"%((pacman[0]+1)%len(lab), pacman[1], pacman[0], pacman[1]))
        if lab[(pacman[0]-1)%len(lab)][pacman[1]]=='+':
            print("movimento do Pac-Man não é possível.")

    if pacman[2]==3:
        if lab[(pacman[0]+1)%len(lab)][pacman[1]]!='+':
            pacman[0]=(pacman[0]+1)%len(lab)
            print("Pac-man moveu-se de (%d,%d) para (%d,%d)"%((pacman[0]-1)%len(lab), pacman[1], pacman[0], pacman[1]))
        if lab[(pacman[0]+1)%len(lab)][pacman[1]]=='+':
            print("movimento do Pac-Man não é possível.")

         
# ======================================================================

def aindaTemPacDots(lab):
    ''' (matriz) -> bool

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!

    Recebe a matriz de caracteres representando o labirinto e devolve
    True se ainda há algum pac-dot no labirinto ou False caso contrário.
    Nada é impresso por essa função.

    !!!VOCÊ PRECISA ESCREVER ESTA FUNÇÃO!!!
    '''
    # escreva sua função a seguir
    achou_pacdot=False
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j]=='.':
                achou_pacdot=True
    return achou_pacdot

# ======================================================================

