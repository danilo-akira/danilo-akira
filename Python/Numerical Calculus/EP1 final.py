
import matplotlib.pyplot as plt    #para traçar gráficos
import math   #para usar o número e no teste inicial 3

#000000000000000000000000000000000000000000000000000000000000000000000000000000   

def LU(A):  #Recebe matriz A e a decompõe em LU
    L = []
    U = []   
    p = []   #matriz permutação
    soma = 0
    m = 0
    s = 0
    #Algoritmo do roteiro do EP
    for x in range(0, len(A)):
        p.append(x)
    for k in range(0,len(A)):
        for i in range(k,len(A)):
            for j in range(0,k):
                soma = soma+A[i][j]*A[j][k]
            A[i][k] = A[i][k]-soma
            soma = 0
            if m<abs(A[i][k]):
                m = abs(A[i][k])
        for l in range(k,len(A)):
            if abs(A[l][k]) == m:
                p[k] = l
        m = 0
        if k != p[k]:
            c = []
            for y in A[k]:
                c.append(y)
            A[k] = A[p[k]]
            A[p[k]] = c
        for j in range(k+1,len(A)):
            for i in range(0,k):
                s = s+A[k][i]*A[i][j]
            A[k][j] = A[k][j]-s
            if A[k][k] != 0:
                A[j][k] = A[j][k]/A[k][k]
            s = 0
    #Matrizes L e U
    for i in range(len(A)):
        L.append([])
        U.append([])
        for j in range(len(A[0])):
            L[i].append(0)
            U[i].append(0)
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j:
                L[i][j] = 1
                U[i][j] = A[i][j]
            elif i<j:
                L[i][j] = 0
                U[i][j] = A[i][j]
            else:
                L[i][j] = A[i][j]
                U[i][j] = 0      
    return(L,U,p)
    
#000000000000000000000000000000000000000000000000000000000000000000000000000000

def sistemalinear(L,U,p,B):     #calcula Ly=B e depois Ux=y
#permuta B
    for i in range(len(B)):
        if i != p[i]:
            copia = B[i][0]
            B[i][0] = B[p[i]][0]
            B[p[i]][0] = copia
    linL = len(L)
    colL = len(L[0])
    linU = len(U)
    colU = len(U[0])
#cria y
    y = []
    for i in range(colL):
        y.append([])
        y[i].append(0)
#calcula y em Ly = B
    for i in range(linL):
        c = 0
        l = 0
        somatorio = 0
        while c<colL:
            if c != i:
                somatorio += L[i][c]*y[l][0]
                c += 1
                l += 1
            else:
                c += 1
                l += 1
        if L[i][i] != 0:
            y[i][0] = (B[i][0]-somatorio)/L[i][i]
#cria x
    x = []    
    for i in range(colU):
        x.append([])
        x[i].append(0)
#calcula x em Ux = y
    for i in range(linU-1,-1,-1):
        c = 0 
        l = 0
        somatorio = 0
        while c<colU:
            if c != i:
                somatorio += U[i][c]*x[l][0]
                c += 1
                l += 1
            else:
                c += 1
                l += 1
        if U[i][i] != 0:
            x[i][0] = (y[i][0]-somatorio)/U[i][i]
    return(x)      

#000000000000000000000000000000000000000000000000000000000000000000000000000000

continua = True
while continua == True:
    print('')
    print('..................................................................................')
    print('')
    print('Digite o problema que quer resolver')
    print('--> 1.2.1 para gráficos do primeiro problema')
    print('--> 1.2 para cálculos e tabelas do primeiro problema')
    print('--> 2 para segundo problema')
    print('--> ti1 para Teste Inicial 1')
    print('--> ti2 para Teste Inicial 2')
    print('--> ti3 para Teste Inicial 3')
    print('--> fim para encerrar o programa')
    print('OBS: se você quiser ver os gráficos, digite fim após o programa mostrar os resultados do item escolhido (1.2.1 ou 2) e retornar ao menu principal')
    problema = input('Problema: ')
                            
    if problema == '1.2.1':
        n = 1
        beta = [0.2,1,2]
        E = 200
        for x in beta:
            c = 0  #contador
            d = []  #deformação
            t = []  #tensão
            i = [y*0.1 for y in range(-10,11)]   #valores de deformação
            for a in i:
                d.append(a)
                t.append(E*(1+x*d[c]**n)*d[c])
                c += 1
            plt.figure(1)
            plt.title('n=1')
            plt.xlabel('Deformação')
            plt.ylabel('Tensão (kN/cm²)')
            plt.axis([-1,1,-200,200])
            plt.plot(d,t,label=r'$\beta$ =%s'%x)
            plt.legend(loc=4)
            
        n = 2
        beta = [5,25,125]
        E = 200
        for x in beta:
            c = 0  #contador
            d = []  #deformação
            t = []  #tensão
            i = [y*0.1 for y in range(-10,11)]   #valores de deformação
            for a in i:
                d.append(a)
                t.append(E*(1+x*d[c]**n)*d[c])
                c += 1
            plt.figure(2)
            plt.title('n=2')
            plt.xlabel('Deformação')
            plt.ylabel('Tensão (kN/cm²)')
            plt.axis([-1,1,-200,200])
            plt.plot(d,t,label=r'$\beta$ =%s'%x)
            plt.legend(loc = 4)
            
    if problema == '1.2':       # Primeiro problema (3 barras)
        A, E, P, l = 0.5,200,5,50   #dados
        beta = float(input('beta= '))
        n = int(input('n= '))
        u1, u2=0, 0  #deformações iniciais
        if beta == 0:   #caso linear
            print('       u1      u2      R3      R4        N1      N2        N3       d1       d2       d3       t1       t2       t3')
        else:
            print('       u1      u2      N1      N2        N3        Resíduo')
        resíduo = [[round(abs(2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) - A*E*(u1/l + beta*(u1/l)**(n+1)) - 8*P),2)], [round(abs(3*A*E*(-u2/l + beta*(-u2/l)**(n+1)) - 2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) + 7*P),2)]]     #resíduo = fi(u) - F
        i = 1   # se o maior valor do resíduo for menor que 10^-6, o loop de iterações para
        while i:   #cálculo das incógnitas
            F = [[-2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) + A*E*(u1/l + beta*(u1/l)**(n+1)) + 8*P],[-3*A*E*(-u2/l + beta*(-u2/l)**(n+1)) + 2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) - 7*P]]
            J = [[-2*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l -A*E*(1+beta*(n+1)*(u1/l)**n)/l, 2*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l], [2*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, -2*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l -3*A*E*(1+beta*(n+1)*(-u2/l)**n)/l]]    #Jacobiano   
            L, U, p = LU(J)
            x1 = sistemalinear(L,U,p,F)[0][0]     
            x2 = sistemalinear(L,U,p,F)[1][0]     
            u1 = u1 + x1   #deslocamento u1
            u2 = u2 + x2   #deslocamento u2
            resíduo = [[round(abs(2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) - A*E*(u1/l + beta*(u1/l)**(n+1)) - 8*P),2)], [round(abs(3*A*E*(-u2/l + beta*(-u2/l)**(n+1)) - 2*A*E*((u2-u1)/l + beta*((u2-u1)/l)**(n+1)) + 7*P),2)]]
            d1, d2, d3 = u1/l, (u2-u1)/l, -u2/l   #deformações
            R3, R4 = -A*E*(d1+beta*d1**(n+1)), 3*A*E*(d3+beta*d3**(n+1))   #reações de apoio
            N1, N2, N3 = A*E*(1+beta*d1**n)*d1, 2*A*E*(1+beta*d2**n)*d2, 3*A*E*(1+beta*d3**n)*d3  #forças normais
            t1, t2, t3 = E*(1+beta*d1**n)*d1, E*(1+beta*d2**n)*d2, E*(1+beta*d3**n)*d3   #tensões
            if beta == 0:
                print('%d   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f'%(i,u1,u2,R3,R4,N1,N2,N3,d1,d2,d3,t1,t2,t3))
            else:
                print('%d   %.3f   %.3f   %.3f   %.3f   %.3f  '%(i,u1,u2,N1,N2,N3),  resíduo)
            i += 1
            if max(resíduo[0][0],resíduo[1][0]) < 10**(-6):   # valor de erro escolhido: 10^-6
                break
        if beta != 0:
            print('')
            print('R3       R4        d1       d2       d3       t1       t2       t3')
            print('%.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f'%(R3,R4,d1,d2,d3,t1,t2,t3))
    
    
    if problema=='2':   # Segundo problema (5 barras)
        A, E, P, l = 0.1, 200, 2, 20   #dados
        beta = int(input('beta= '))
        n = int(input('n= '))
        u1, u2, u3 = 0,0,0  #deformações iniciais
        print('      u1      u2     u3     N1      N2       N3      N4       N5      Resíduo')
        tensao2 = []  #depois de rodar o programa, vimos que as barras 2 e 5 são as mais solicitadas, por isso criamos essas variáveis que serão usadas para traçar os gráficos
        tensao5 = []
        def2 = []
        def5 = []
        resíduo = [[round(abs(-P + 2*A*E*((u1)/l+beta*((u1)/l)**(n+1)) - A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) - 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1))), 3)], [round(abs(-2*P + 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1)) - 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))), 3)], [round(abs(-3*P + A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) + 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1)) - 5*A*E*((-u3)/l+beta*((-u3)/l)**(n+1))), 3)]]
        i = 1  #interação
        while i:   #cálculo das incógnitas
            F = [[P-2*A*E*((u1)/l+beta*((u1)/l)**(n+1)) + A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) + 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1))], [2*P-3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1)) +4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))], [3*P- A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) - 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))+ 5*A*E*((-u3)/l+beta*((-u3)/l)**(n+1))]]
            J = [[2*A*E*(1+beta*(n+1)*((u1)/l)**n)/l + A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) + 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, -3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, -A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l)], [-3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l], [-A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l), -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l +5*A*E*(1+beta*(n+1)*((-u3)/l)**n)/l]]   #Jacobiano
            L, U, p = LU(J)
            x1 = sistemalinear(L,U,p,F)[0][0]     
            x2 = sistemalinear(L,U,p,F)[1][0]
            x3 = sistemalinear(L,U,p,F)[2][0]
            u1 = u1 + x1   #deslocamento u1
            u2 = u2 + x2   #deslocamento u2
            u3 = u3 + x3   #deslocamento u3
            resíduo = [[round(abs(-P + 2*A*E*((u1)/l+beta*((u1)/l)**(n+1)) - A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) - 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1))), 3)], [round(abs(-2*P + 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1)) - 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))), 3)], [round(abs(-3*P + A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) + 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1)) - 5*A*E*((-u3)/l+beta*((-u3)/l)**(n+1))), 3)]]
            d1, d2, d3, d4, d5 = (u3-u1)/(2*l), (u1)/l, (u2-u1)/l, (u3-u2)/l, (-u3)/l   #deformações
            R4, R5 = -2*A*E*(1+beta*d2**n)*d2, 5*A*E*(1+beta*d5**n)*d5   #reações de apoio
            N1, N2, N3, N4, N5 = A*E*(1+beta*d1**n)*d1, 2*A*E*(1+beta*d2**n)*d2, 3*A*E*(1+beta*d3**n)*d3, 4*A*E*(1+beta*d4**n)*d4, 5*A*E*(1+beta*d5**n)*d5 #forças normais
            t1, t2, t3, t4, t5 = E*(1+beta*d1**n)*d1, E*(1+beta*d2**n)*d2, E*(1+beta*d3**n)*d3, E*(1+beta*d4**n)*d4, E*(1+beta*d5**n)*d5    #tensões
            print('%d   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f '%(i,u1,u2,u3,N1,N2,N3,N4,N5),  resíduo)
            i += 1
            if max(resíduo[0][0],resíduo[1][0],resíduo[2][0]) < 10**(-6):
                break
        print('')
        print(' R4        R5       d1      d2      d3       d4       d5      t1       t2      t3       t4      t5')
        print('%.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f   %.3f'%(R4,R5,d1,d2,d3,d4,d5,t1,t2,t3,t4,t5))
                
    # Depois de rodar o programa, vimos que as barras 2 e 5 são as mais solicitadas
        u1, u2, u3 = 0, 0, 0
        tensao2 = []
        tensao5 = []
        def2 = []
        def5 = []
        if n == 1 and beta == 3:
            P = [0.1*y for y in range(0,17)]    #valores de 0,1 em 0,1 entre 0 e 1,6 kN
            for a in P:
                F = [[a-2*A*E*((u1)/l+beta*((u1)/l)**(n+1)) + A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) + 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1))], [2*a-3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1)) +4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))], [3*a- A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) - 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))+ 5*A*E*((-u3)/l+beta*((-u3)/l)**(n+1))]]
                J = [[2*A*E*(1+beta*(n+1)*((u1)/l)**n)/l + A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) + 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, -3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l)], [-3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l], [-A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l), -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l +5*A*E*(1+beta*(n+1)*((-u3)/l)**n)/l]]
                L, U, p = LU(J)
                x1 = sistemalinear(L,U,p,F)[0][0]     
                x3 = sistemalinear(L,U,p,F)[2][0]
                u1 = u1+x1   #deslocamento u1
                u3 = u3+x3   #deslocamento u3
                d2, d5 = (u1)/l,(-u3)/l   #deformações
                def2.append(d2)
                def5.append(d5)
                t2, t5 = E*(1+beta*d2**n)*d2, E*(1+beta*d5**n)*d5    #tensões
                tensao2.append(t2)
                tensao5.append(t5)
            plt.figure(1)
            plt.title('n=1, beta=3')
            plt.xlabel('P (kN)')
            plt.ylabel('Deformação')
            plt.axis([0,2,-0.15,0.1])
            plt.plot(P,def2,label='Barra 2')
            plt.plot(P,def5,label='Barra 5')
            plt.legend(loc=4)
            plt.figure(2)
            plt.title('n=1, beta=3')
            plt.xlabel('P (kN)')
            plt.ylabel('Tensão (kN/cm²)')
            plt.axis([0,2,-20,20])
            plt.plot(P,tensao2,label='Barra 2')
            plt.plot(P,tensao5,label='Barra 5')
            plt.legend(loc=2)
                
        if n == 2 and beta == 125:
            P = [0.1*y for y in range(0,41)]
            for a in P:
                F = [[a-2*A*E*((u1)/l+beta*((u1)/l)**(n+1)) + A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) + 3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1))], [2*a-3*A*E*((u2-u1)/l+beta*((u2-u1)/l)**(n+1)) +4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))], [3*a- A*E*((u3-u1)/(2*l)+beta*((u3-u1)/(2*l))**(n+1)) - 4*A*E*((u3-u2)/l+beta*((u3-u2)/l)**(n+1))+ 5*A*E*((-u3)/l+beta*((-u3)/l)**(n+1))]]
                J = [[2*A*E*(1+beta*(n+1)*((u1)/l)**n)/l + A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) + 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, -3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l)], [-3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l, 3*A*E*(1+beta*(n+1)*((u2-u1)/l)**n)/l +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l], [-A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l), -4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l, A*E*(1+beta*(n+1)*((u3-u1)/(2*l))**n)/(2*l) +4*A*E*(1+beta*(n+1)*((u3-u2)/l)**n)/l +5*A*E*(1+beta*(n+1)*((-u3)/l)**n)/l]] 
                L,U,p=LU(J)
                x1 = sistemalinear(L,U,p,F)[0][0]     
                x2 = sistemalinear(L,U,p,F)[1][0]
                x3 = sistemalinear(L,U,p,F)[2][0]
                u1 = u1+x1   #deslocamento u1
                u3 = u3+x3   #deslocamento u3
                d2, d5 = (u1)/l, (-u3)/l   #deformações
                def2.append(d2)
                def5.append(d5)
                t2,t5=E*(1+beta*d2**n)*d2, E*(1+beta*d5**n)*d5    #tensões
                tensao2.append(t2)
                tensao5.append(t5)
            plt.figure(1)
            plt.title('n=2, beta=125')
            plt.xlabel('P (kN)')
            plt.ylabel('Deformação')
            plt.axis([0,2,-0.15,0.1])
            plt.plot(P,def2,label='Barra 2')
            plt.plot(P,def5,label='Barra 5')
            plt.legend(loc=4)
            plt.figure(2)
            plt.title('n=2, beta=125')
            plt.xlabel('P (kN)')
            plt.ylabel('Tensão (kN/cm²)')
            plt.axis([0,5,-40,40])
            plt.plot(P,tensao2,label='Barra 2')
            plt.plot(P,tensao5,label='Barra 5')
            plt.legend(loc=2)
            
    
    if problema=='ti1':
        x, y = 0, 0 
        resíduo = [[abs(2*x - 4)],[abs(2*y - 6)]]
        i = 1
        while i:
            F = [[-2*x+4],[-2*y+6]]
            J = [[2,0],[0,2]]
            L, U, p = LU(J)
            x = x + sistemalinear(L,U,p,F)[0][0]     
            y = y + sistemalinear(L,U,p,F)[1][0]     
            resíduo = [[abs(2*x - 4)],[abs(2*y - 6)]]
            print(' x      y')
            print('%.2f    %.2f'%(x,y))        
            i += 1
            if max(resíduo[0][0], resíduo[1][0]) < 10**(-6):
                break
            
        print('')
        print('O ponto de mínimo da função F(x,y) = (x-2)² + (y-3)² é: ')
        print('')
        print('(x, y) = (%.2f, %.2f)'%(x,y))
        
        
    if problema=='ti2':
        i=1
        x1, x2, x3, x4 = 1, 1, 1, 1
        resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
        print(' i      x1         x2         x3         x4        resíduo')
        while i:    #cálculo da F, J e das incógnitas x1, x2, x3 e x4
            F = [[-4*x1 + x2 - x3 + x1*x4], [x1 - 3*x2 + 2*x3 + x2*x4], [-x1 + 2*x2 - 3*x3 + x3*x4], [-(x1**2) - (x2**2) - (x3**2) + 1]] 
            J = [[4-x4, -1, 1, -x1], [-1, 3-x4, -2, -x2], [1, -2, 3-x4, -x3], [2*x1, 2*x2, 2*x3, 0]] 
            L, U, p = LU(J)
            c1 = sistemalinear(L,U,p,F)[0][0]
            F = [[-4*x1 + x2 - x3 + x1*x4], [x1 - 3*x2 + 2*x3 + x2*x4], [-x1 + 2*x2 - 3*x3 + x3*x4], [-(x1**2) - (x2**2) - (x3**2) + 1]]
            resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
            c2 = sistemalinear(L,U,p,F)[1][0]
            F = [[-4*x1 + x2 - x3 + x1*x4], [x1 - 3*x2 + 2*x3 + x2*x4], [-x1 + 2*x2 - 3*x3 + x3*x4], [-(x1**2) - (x2**2) - (x3**2) + 1]] 
            resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
            c3 = sistemalinear(L,U,p,F)[2][0]
            F = [[-4*x1 + x2 - x3 + x1*x4], [x1 - 3*x2 + 2*x3 + x2*x4], [-x1 + 2*x2 - 3*x3 + x3*x4], [-(x1**2) - (x2**2) - (x3**2) + 1]] 
            resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
            c4 = sistemalinear(L,U,p,F)[3][0]
            F = [[-4*x1 + x2 - x3 + x1*x4], [x1 - 3*x2 + 2*x3 + x2*x4], [-x1 + 2*x2 - 3*x3 + x3*x4], [-(x1**2) - (x2**2) - (x3**2) + 1]] 
            resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
            x1 = x1 + c1
            x2 = x2 + c2
            x3 = x3 + c3
            x4 = x4 + c4
            resíduo = [[abs(4*x1 - x2 + x3 - x1*x4)], [abs(-x1 + 3*x2 - 2*x3 - x2*x4)], [abs(x1 - 2*x2 + 3*x3 - x3*x4)], [abs((x1**2) + (x2**2) + (x3**2) - 1)]]
            print(' %d    %f   %f   %f   %f  '%(i,x1,x2,x3,x4),resíduo)
            if max(resíduo[0][0], resíduo[1][0], resíduo[2][0], resíduo[3][0]) < 10**(-6):
                break
            
        print('')
        print ('Dada a função F(x1, x2, x3, x4) = (4x1 - x2 + x3 - x1.x4, -x1 + 3.x2 - 2.x3 - x2.x4, x1 - 2.x2 + 3.x3 - x3.x4, x1² + x2² + x3² - 1), sendo x = (1,1,1,1) como valor inicial, temos que a raiz é:')
        print('')
        print('x1 = %.2f , x2 = %.2f , x3 = %.2f , x4 = %.2f'%(x1,x2,x3,x4))
        
    if problema=='ti3':
        n = int(input('n = '))
        F = []
        J = []
        x = []
        linha = []
        resíduo = []
    # cria a matriz x, F e resíduo com base no número n definido
        for i in range(n-1):
            x.append([0])
            F.append([0])
            resíduo.append([0])
            linha = []
            for k in range(n-1):
                linha.append(0)
            J.append(linha)
    # preenche a matriz F 
        for i in range(0, n-1):
            if i == 0:
                F[i][0] = -2*x[0][0] + x[1][0] + math.exp(x[0][0])/(n**2)
            if 0 < i < n-2:
                F[i][0] = x[i-2][0] - 2*x[i-1][0] + x[i][0] + math.exp(x[i-1][0])/(n**2)
            if i == n-2:
                F[i][0] = x[n-3][0] - 2*x[n-2][0] + math.exp(x[n-2][0])/(n**2)
        for i in range(len(resíduo)):
            resíduo[i][0] = abs(F[i][0])
        
        #preenche a matriz Jacobiana
        for i in range(1, n):
            if i == 1:
                J[i-1][i-1] = 2 - math.exp(x[1][0])/(n**2)
                J[i-1][i] = -1
            elif 1 < i < n-1:
                J[i-1][i-2] = -1
                J[i-1][i-1] = 2 - math.exp(x[i][0])/(n**2)
                J[i-1][i] = -1
            elif i == n-1:
                J[i-1][i-2] = -1
                J[i-1][i-1] = 2 - math.exp(x[i-1][0])/(n**2)
        #calcula as variáveis x
        L, U, p = LU(J)
        for i in range(0, n-1):
            c = sistemalinear(L, U, p, F)
            x[i][0] = x[i][0] + c[i][0]
            print('x%d = %f'%(i+1,x[i][0]))
            
    if problema == 'fim':
        print('Obrigado! Volte sempre =)')
        continua = False
        

        
            




