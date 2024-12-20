#Soluciones por Pablo Moreno Moreu, Arnau Neches Vila, Carlos Fernandez-LLebrez Acedo
def lee_numero():
    return int(input())

def lee_numeros():
    return list(map(int, input().split()))

def solve(nMax: int, ls:list):
    #posibles precios distintos: hay que hacer todas las sumas posibles de hasta nMax monedas
    #RECURSIVOOOOO
    #Si esto no es muy eficiente (que no lo es): se puede añadir memoria
    resSet = set()
    solveRes(nMax, ls, resSet, 0)
    print(len(resSet))


#Como añadir memoria, que estoy vago como pa escribirlo: quitamos el ls+[0] y añadimos siempre a resSet. Metemos tuplas con el 
#numero y paso de nMax. Si ya estaba esa tupla, cortamos la rama. Al final casi solo se exploran tantas ramas como soluciones hay, eficiencia maxima!!!
def solveRes(nMax: int, ls: list, resSet: set, currSum: int):
    if nMax == 1:
        for e in ls:
            resSet.add(e+currSum)
    else:
        for e in ls + [0]: #para conseguir soluciones con menos de nMax monedas
            solveRes(nMax-1,ls,resSet,currSum+e)

def main():
    n = lee_numero()
    while n != 0:
        solve(lee_numeros()[1], lee_numeros())
        n-=1

if __name__ == "__main__":
    main()