def citireLista():
  l = []
  n = int(input("Dati nr. de elemente din lista"))
  for i in range (1 , n):
    givenString = input("Elementul" + i + ":")
  numbersAsString = givenString.split(",")
  for x in numbersAsString:
    l.append(int(x))
  return l