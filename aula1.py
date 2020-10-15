#Exercicio 1.1
def comprimento(lista):
	if not lista:
		return 0
	return 1 + comprimento(lista[1:])




#Exercicio 1.2
def soma(lista):
	if len(lista)>0:
		sum = lista[0]
		sum += soma(lista[1:])
		return sum
	return 0

#Exercicio 1.3
def existe(lista, elem):
	if len(lista)>0:
		if lista[0] == elem:
			return True
		else:
			return existe(lista[1:], elem)
	return False


#Exercicio 1.4
def concat(l1, l2):
	if len(l2)>0:
		l1.append(l2[0])
		l2.pop(0)
		return concat(l1,l2)
	return l1


#Exercicio 1.5
def inverte(lista):
	final = []

	if len(lista)>=1:
		final.append(lista[-1])
		lista.pop(-1)
		if len(lista)!=0:
			inv = inverte(lista)
			for elem in inv:
				final.append(elem)
		return final



#Exercicio 1.6
def capicua(lista):
	if len(lista)>=1:
		a = lista[0]
		b = lista[-1]

		if a == b:
			if len(lista)>2:
				lista.pop(0)
				lista.pop(-1)
				capicua(lista)
			return True
	return False


#Exercicio 1.7
def explode(lista):
	if len(lista)>1:
		final = concat(lista[0], lista[1])
		lista[0] = final
		lista.pop(1)
		return explode(lista)

	return lista[0]


#Exercicio 1.8
def substitui(lista, original, novo):
	if len(lista)>0:
		if lista[0]==original:
			lista[0]=novo
		if len(lista)==1:
			return lista
		else:
			return concat([lista[0]],(substitui(lista[1:],original,novo)))




#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	if len(lista2)>0:
		elem = lista2[0]
		lista2.pop(0)

		for i in lista1:
			if  i >= elem:
				index = lista1.index(i)
				lista1.insert(index,elem)
				break
		if elem not in lista1:
			lista1.append(elem)

		lista1 =junta_ordenado(lista1,lista2)
	return lista1

#Exercicio 1.10


#Exercicio 2.1
def separar(lista):
	if len(lista)>0:
		elem = lista[0]
		an = elem[0]
		bn = elem[1]
		rest = [[],[]]
		if len(lista)>1:
			rest = separar(lista[1:])

		rest[0].append(an)
		rest[1].append(bn)

		return (sorted(rest[0]),sorted(rest[1]))


#Exercicio 2.2
def remove_e_conta(lista, elem):
	if len(lista)>0:
		n = 0
		if lista[0]==elem:
			n+=1
			lista.pop(0)
			res = remove_e_conta(lista,elem)
			return (res[0], n+res[1])
		else:
			res = remove_e_conta(lista[1:],elem)
			lista[1:] = res[0]
			return(lista,res[1])


	return (lista,0)

#Exercicio 2.3
def ocorrencias(lista):
	if len(lista)>1:
		elem =lista[0]
		res = remove_e_conta(lista,elem)
		cont =(elem,res[1])
		if len(res[0])>0:
			rest = ocorrencias(res[0])
			return (cont,rest[0])

	elif len(lista)==1:
		return[lista[0],1]


#Exercicio 3.1
def cabeca(lista):
	if not lista:
		return None
	else:
		return lista[0]

#Exercicio 3.2
def cauda(lista):
	if len(lista)<=1:
		return None
	else:
		return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1)!=len(l2):
		return None
	if not l1:
		return []
	return [(l1[0],l2[0])] + juntar(l1[1:], l2[1:])


#Exercicio 3.4
def menor(lista):
	if not lista:
		return None
	if len(lista)>=2:
		if lista[1]<=lista[0]:
			lista.pop(0)
			return menor(lista)
		else:
			lista.pop(1)
			return menor(lista)
	if len(lista)==1:
		return lista[0]
#Exercicio 3.5
def min_par(lista):
	if not lista:
		return None
	temp = lista
	lista = remove_e_conta(lista, menor(temp))
	return (menor(temp), lista[0])
#Exercicio 3.6
def maior(lista):
	if not lista:
		return None
	if len(lista)>=2:
		if lista[1]>lista[0]:
			lista.pop(0)
			return maior(lista)
		else:
			lista.pop(1)
			return maior(lista)
	if len(lista)==1:
		return lista[0]

def max_min(lista):
	if not lista:
		return None
	return (menor(lista), maior(lista))

#Exercicio 3.7
def men_lista(lista):
	if not lista:
		return None
	min1 = menor(lista)
	new_lista = remove_e_conta(lista, min1)
	min2 = menor(new_lista[0])
	return (min1,min2, remove_e_conta(new_lista[0],min2)[0])

#Exercicio 3.8


def med_med(lista):
	sum = soma(lista)
	media = sum/len(lista)
	mid = len(lista)/2
	if len(lista)%2==0:
		mediana = lista[mid]
	else:
		lower = mid.round()
		mediana = lista[lower+1]
	return (media,mediana)
