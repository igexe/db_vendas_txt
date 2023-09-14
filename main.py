import cadastro_vendedor as vendedor

vendedor.cadastro()

t=open('vendedor.txt','r')
r=t.readlines()

for x in r:
    x=x.rstrip('\n')
    x=eval(x)
    print(x)