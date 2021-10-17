def citireLista():
  l = []
  n = int(input("Dati nr. de elemente din lista"))
  for i in range (0 , n):
    givenString = input("Elementul" + str(i) + ":")
    l.append(givenString)
  return l

def EsteSirulInLista(l):
  element = input("Dati sirul cautat ")
  if element in l :
    print("DA")
  else :
    print("NU")

def EsteDuplicat(l) :
  aparitie = dict()
  raspuns = []
  for element in l :
    if element in aparitie :
      aparitie[element] +=1
    else :
      aparitie[element] = 1
  for sir ,nr in aparitie.items() :
    if nr>=2 :
      raspuns.append(sir)
  if raspuns :
    return raspuns
  else :
    return "UNIC"
if __name__=='__main__' :
  lista=[]
  while True :
      raspuns = input("1. Citire\n 2.Verifica sirul in lista\n 3.Verifica duplicate\n4.Iesire\n")
      if raspuns == "1" :
        lista=citireLista()
      if raspuns == "2" :
        EsteSirulInLista(lista)
      if raspuns == "3" :
        x=EsteDuplicat(lista)
        print(x)
      if raspuns == "4" :
        break

