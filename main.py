import cadastro_cliente as cliente

#cliente.cadastro()

t=open('clientes.txt','r')
d=t.readlines()

for x in d:
    print(x.rstrip('\n'))