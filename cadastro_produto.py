def cadastro():

    id=0
    produtos=[]

    txt=open('produto.txt','r')
    dados=txt.readlines()

    if int(dados[0])!=0:
        id=int(dados[0])
        for x in dados!=dados[0]:
            x=x.rstrip('\n')
            x=x.eval
            produtos.append(x)
    else:
        id=0
    txt.close()

    id+=1

    produtos.append({
        'id':id,
        'produto':input('\ndigite o nome do produto\n'),
        'valor':float(input('\ndigite o valor do produto\n'))
    })

    linha=str(id)+'\n'
    for x in produtos:
        linha+=str(x)+'\n'

    txt=open('produto.txt','w')
    txt.writelines(linha)