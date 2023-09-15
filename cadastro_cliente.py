def cadastro():

    id=0
    lst=[]

    txt=open('cliente.txt','r')
    dados=txt.readlines()

    if int(dados[0])!=0:
        id=int(dados[0])
        for x in dados!=dados[0]:
            x=x.rstrip('\n')
            x=eval(x)
            lst.append(x)
    else:
        id=0

    txt.close()

    id+=1

    lst.append({
        'id':id,
        'nome':input('\nnome cliente\n')
    })

    linha=str(id)+'\n'

    for x in lst:
        linha+=str(x)+'\n'

    txt=open('clientes.txt','w')
    txt.writelines(linha)