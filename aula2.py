import math
#Exercicio 4.1
impar = lambda x:x%2!=0

#Exercicio 4.2
positivo = lambda x:x>0

#Exercicio 4.3
comparar_modulo = lambda x,y:abs(x)<abs(y)

#Exercicio 4.4
cart2pol = lambda x,y: (math.sqrt(x**2 + y**2), math.atan2(y,x))

#Exercicio 4.5
def ex5(f,g,h):
    return lambda x,y,z: h(f(x,y),g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if False in [(lambda x:f(x))(x) for x in lista]:
        return False 
    return True

#Exercicio 4.7
def quantificador_existencial(lista, f):
    if True in [(lambda x:f(x))(x) for x in lista]:
        return True 
    return False

#Exercicio 4.8
def contains(lista1,lista2):
    if False in[(lambda x: x in lista2)(x) for x in lista1]:
        return False
    return True

#Exercicio 4.9
def ordem(lista, f):
    if not lista:
        return []
    if len(lista)==1:
        return lista[0]
    else:
        x = lista[0]
        y = lista[1]
        if f(x,y):
            lista.pop(1)
        else:
            lista.pop(0)
        return ordem(lista,f)
        

#Exercicio 4.10
def filtrar_ordem(lista, f):
    lista=sorted(lista, key=[[(lambda x,y: f(x,y)) for x in lista] for y in lista])
    print(lista)

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
