def cadastro():

    id=0
    vendedores=[]

    txt=open('vendedor.txt','r')
    dados=txt.readlines()

    if int(dados[0])!=0:
        id=dados[0]
        for x in dados!=dados[0]:
            vendedores.append(x)
    else:
        pass
    txt.close()

    id+=1

    vendedores.append({
        'id':id,
        'nome':input('\ndigite o nome do vendedor\n')
        })
    
    txt=open('vendedor.txt','w')

    linha=str(id)+'\n'
    
    for x in vendedores:
        linha+=str(x)+'\n'
    txt.writelines(linha)

    txt.close()