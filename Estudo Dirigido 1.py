#Estudo Dirigido 1: Calculadora Vetorial
#Universidade Federal do Rio de Janeiro
#DMA/IM - Departamento de Matematica Aplicada do Instituto de Matematica
#Top. Mat. Aplicada A - Programacao I
#Professor: Milton Ramirez
#Aluna: Júlia Brito de Freitas
#DRE: 117050512
#email: juliafreitas@poli.ufrj.br
#https://github.com/juliabrfreitas?tab=repositories

def Menu():
    print ('''\n Menu de Opcoes: \n 1-Soma Vetores \n 2-Multiplicação por um escalar \n 3-Combinação Linear
 4-Produto Interno \n 5-Norma Vetorial \n 6-Distância entre dois vetores \n 7-Angulo entre dois vetores
 8-Alterar dimensao dos vetores\n 9-Memorizar Resultado \n 10-Sair \n''') 

def Opcao():
    while True:
        Menu()
        dim=3
        n=input("Digite a opção aqui \n")
        if n=='10':
            break
        elif n=='8':
            dim=int(input("Digite a dimensão dos vetores aqui \n"))
        elif n=='9':
            acumulador=result
        else:
            v1=[]
            v2=[]
            if n=='1' or n=='3' or n=='4' or n=='6' or n=='7':
                for i in range(dim):
                    x=input("Digite a coordenada do primeiro vetor aqui ou tecle r para usar o resultado gravado\n")
                    if x=='r':
                        x=acumulador
                    else:
                        try:
                            x=float(x)
                        except ValueError:
                            print ("Opção Inválida"); Opcao()
                        v1.append(x)
                for i in range(dim):
                    y=float(input("Digite a coordenada do segundo vetor aqui ou tecle r para usar o resultado gravado\n"))
                    if y=='r':
                        y=acumulador
                    else:
                        try:
                            y=float(y)
                        except ValueError:
                            print ("Opção Inválida"); Opcao()
                        v2.append(y)            
                if n=='1':
                    print (Soma(v1,v2))
                if n=='3':
                    c1==input("Digite a constante que multiplicará o primeiro vetor ou tecle r para usar o resultado gravado\n")
                    if c1=='r':
                        c1=acumulador
                    else:
                        try:
                            c1=float(c1)
                        except ValueError:
                            print ("Opção Inválida"); Opcao()
                    c2==input("Digite a constante que multiplicará o segundo vetor ou tecle r para usar o resultado gravado\n")
                    if c2=='r':
                        c2=acumulador
                    else:
                        try:
                            c2=float(c2)
                        except ValueError:
                            print ("Opção Inválida"), Opcao()
                    result=MultiEscalar(v1,c1)+MultiEscalar(v2,c2)
                    print (result)
                if n=='4':
                    print (ProdutoInterno(v1,v2))
                if n=='7':
                    print (ProdutoInterno(v1,v2)/(Modulo(v1)*Modulo(v2)))
                if n=='6':
                    v1=MenosUm(v1)
                    print (v1)
                    result=Modulo(Soma(v1,v2))
                    print (result)                    
            elif n=='2' or n=='5':
                for i in range(dim):
                    x=float(input("Digite a coordenada do vetor aqui ou tecle r para usar o resultado gravado\n"))
                    if x=='r':
                        x=acumulador
                    else:
                        try:
                            x=float(x)
                        except ValueError:
                            print ("Opção Inválida"); Opcao()
                        v1.append(x)
                if n=='2':
                    c=float(input("Digite a constante aqui ou tecle r para usar o resultado gravado\n"))
                    if c=='r':
                        c=acumulador
                    else:
                        try:
                            c=float(c)
                        except ValueError:
                            print ("Opção Inválida"); Opcao()
                    print (MultiEscalar(v1,c))
                if n=='5':
                    print (Modulo(v1))
            else:
                print ("Opção Inválida"); Opcao()



def MenosUm(v):
    listam=[]
    for i in range(len(v)):
        listam.append(v[i]*(-1))
    return listam                

def Soma(v1,v2):
    lista=[]
    for i in range(len(v2)):
        lista.append(v1[i]+v2[i])
    result=lista
    return result   

def MultiEscalar(v,c):
    result=c*v
    return result

def Modulo(v):
    cont=0
    for i in range(len(v)):
        cont+=v[i]**2
        print (cont)
    result=cont**0.5
    return result

def ProdutoInterno(v1,v2):
    cont=0
    for i in range(len(v1)):
        cont+=v1[i]*v2[i]
    result=cont
    return result    
      
Opcao()
