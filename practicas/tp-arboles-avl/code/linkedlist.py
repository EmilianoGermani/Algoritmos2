class LinkedList:
  head=None
class Node:
  value=None
  nextNode=None

class NodeTree:
  value=None
  key=None
  nextNode=None

#Subprograma que agrega un elemento al inicio de la lista
def addTree(L,element,key):
  if L.head==None:
    L.head=NodeTree()
    L.head.value=element
    L.head.key=key
  else:
    NewNode=NodeTree()
    NewNode.value=element
    NewNode.key=key
    NewNode.nextNode=L.head
    L.head=NewNode

#Subprograma que muestra en pantalla la lista
def printlist(L):
  if L!=None:
    currentNode=L.head
    while currentNode!=None:
      print(currentNode.value, end=" -> ")
      currentNode=currentNode.nextNode
    print(" ")
  else:
    return None

#Subprograma que invierte la lista L
def invertirlista(L):
  cont=length(L)
  while cont>1:
    currentNode=L.head
    for i in range(0,length(L)-1):
      currentNode=currentNode.nextNode
    Node=deletePosition(L,cont-2)
    Node.nextNode=currentNode.nextNode
    currentNode.nextNode=Node
    cont=cont-1
  return L

#Subprograma que agrega un elemento al inicio de la lista
def add(L,element):
  if L.head==None:
    L.head=Node()
    L.head.value=element
  else:
    NewNode=Node()
    NewNode.value=element
    NewNode.nextNode=L.head
    L.head=NewNode

#Subprograma que devuelve la posicion del elemento buscado o None si no se encuentra dicho elemento
def search(L,element):
  if L.head==None:
    return None
  else:
    currentNode=L.head
    cont=0
    while currentNode!=None:
      if currentNode.value==element:
        return cont
      else:
        currentNode=currentNode.nextNode
        cont=cont+1
    return None

#Subprograma que devuelve la cantidad de elementos que se encuentran en la Lista
def length(L):
  if L.head==None:
    return 0
  else:
    cont=0
    currentNode=L.head
    while currentNode!=None:
      currentNode=currentNode.nextNode
      cont=cont+1
    return cont

#Subprograma que inserta un elemento en la posicion especificada y devuelve la posicion donde se inserto, si la posicion especificada excede al tamaño de la lista devuelve None
def insert(L,element,position):
  if position==0:
    add(L,element)
    return 0
  elif position>length(L):
    print ("Posicion ingresada excede el tamaño de la lista")
    return None
  else:
    cont=0
    currentNode=L.head
    while position-1>cont:
      currentNode=currentNode.nextNode
      cont=cont+1
    if currentNode.nextNode!=None:
      NewNode=Node()
      NewNode.value=element
      NewNode.nextNode=currentNode.nextNode
      currentNode.nextNode=NewNode
      return position
    else:
      NewNode=Node()
      NewNode.value=element
      currentNode.nextNode=NewNode
      return position

#Subprograma que elimina un Nodo donde se encuentre el elemento especificado y devuelve la posicion donde se encontraba, en caso de no encontrarse el elemento devuelve None
def delete(L,element):
  if search(L,element)==None:
    return None
  elif search(L,element)==0:
    position=search(L,element)
    L.head=L.head.nextNode
    return position
  else:
    position=search(L,element)
    cont=0
    currentNode=L.head
    while position-1>cont:
      currentNode=currentNode.nextNode
      cont=cont+1
    if currentNode.nextNode.nextNode!=None:
      currentNode.nextNode=currentNode.nextNode.nextNode
    else:
      currentNode.nextNode=None
    return position

#Subprograma que elimina el nodo de la posicion ingresada y devuelve el elemento que se encontraba en dicho nodo, en caso que la posicion elegida sea mayor que el tamaño de la lista devuelve None
def deletePosition(L,position):
  if position>=length(L):
    print ("Posicion excedida")
    return None
  if position==0:
    element=L.head
    L.head=L.head.nextNode
    return element
  else:
    currentNode=L.head
    for i in range(0,position-1):
      currentNode=currentNode.nextNode
    element=currentNode.nextNode
    if currentNode.nextNode.nextNode!=None:
      currentNode.nextNode=currentNode.nextNode.nextNode
    else:
      currentNode.nextNode=None
    return element

#Subprograma que devuelve el elemento que se encuentre en la posicion especificada, en caso de que la posicion especificada exceda el tamaño de la lista devuelve None
def access(L,position):
  if position>=length(L):
    print ("Posicion ingresada excede el tamaño de la lista")
    return None
  else:
    cont=0
    currentNode=L.head
    while position>cont:
      currentNode=currentNode.nextNode
      cont=cont+1
    return currentNode.value

#Subprograma que reemplaza el elemento en el Nodo con la posicion especificada y devuelve la posicion donde lo hizo, en caso de que la posicion especificada exceda el tamaño de la lista devuelve None
def update(L,element,position):
  if position>=length(L):
    print ("Posicion ingresada excede el tamaño de la lista")
    return None
  else:
    cont=0
    currentNode=L.head
    while position>cont:
      currentNode=currentNode.nextNode
      cont=cont+1
    currentNode.value=element
    return position

#Subprograma que intercambia de posicion los elementos que se encuentren en la posicion "pos1" y la posicion "pos2"
def moveNode(L,pos1,pos2):
  if pos1>=length(L) or pos2>=length(L):
    print("posicion elegida excede el tamaño de la lista")
    return None
  elif pos1==pos2:
    print ("datos ingresados incorrectos")
    return None
  elif pos1>pos2:
    aux=pos1
    pos1=pos2
    pos2=aux
  currentNode=L.head
  for i in range(0,pos2):
    currentNode=currentNode.nextNode
  Node1=deletePosition(L,pos1)
  Node1.nextNode=currentNode.nextNode
  currentNode.nextNode=Node1
  Node2=deletePosition(L,pos2-1)
  if pos1==0:
    Node2.nextNode=L.head
    L.head=Node2
  else:
    currentNode=L.head
    for i in range(0,pos1-1):
      currentNode=currentNode.nextNode
    Node2.nextNode=currentNode.nextNode
    currentNode.nextNode=Node2
  return L