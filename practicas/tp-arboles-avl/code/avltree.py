#from algo1 import *
import linkedlist
from myqueue import *

def test(currentNode):
  if currentNode!=None:
    print("el Nodo ",currentNode.value," tiene BF=",currentNode.bf)
    test(currentNode.leftnode)
    test(currentNode.rightnode)

class AVLTree:
  root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


#Subprograma que realiza la rotacion de un Nodo hacia la derecha
def rotateRight(B,avlnode):
  if avlnode.parent!=None: #Caso que NO es la Raiz
    if avlnode.parent.key>avlnode.key: #Verifica la key del padre para saber si sera hijo izquierdo o derecho
      avlnode.parent.leftnode=avlnode.leftnode
      avlnode.leftnode.parent=avlnode.parent
    else:
      avlnode.parent.rightnode=avlnode.leftnode
      avlnode.leftnode.parent=avlnode.parent
    avlnode.parent=avlnode.leftnode #Asigno como padre del nodo a su hijo izquierdo
    if avlnode.parent.rightnode!=None: #Caso en el que el hijo izquierdo tenia un hijo derecho
      avlnode.leftnode=avlnode.parent.rightnode
      avlnode.parent.rightnode.parent=avlnode
    else: #caso contrario se le asigna None
      avlnode.leftnode=None
    avlnode.parent.rightnode=avlnode   
  else: #Caso en el que es la Raiz
    #print("es la raiz")
    B.root=avlnode.leftnode
    avlnode.leftnode.parent=None
    avlnode.parent=avlnode.leftnode
    if avlnode.parent.rightnode!=None: #Caso en el que el hijo izquierdo tenia un hijo derecho
      avlnode.leftnode=avlnode.parent.rightnode
      avlnode.parent.rightnode.parent=avlnode
    else:
      avlnode.leftnode=None
    avlnode.parent.rightnode=avlnode
  return B

#Subprograma que realiza la rotacion de un Nodo hacia la izquierda
def rotateLeft(B,avlnode):
  if avlnode.parent != None: #Caso que no es la Raiz
    if avlnode.parent.key>avlnode.key: #Verifica la key del padre para saber si sera hijo izquierdo o derecho
      avlnode.parent.leftnode=avlnode.rightnode
      avlnode.rightnode.parent=avlnode.parent
    else:
      avlnode.parent.rightnode=avlnode.rightnode
      avlnode.rightnode.parent=avlnode.parent
    avlnode.parent=avlnode.rightnode #Asigno como padre del nodo a su hijo derecho
    if avlnode.parent.leftnode!=None: #Caso en el que el hijo derecho tenia un hijo izquierdo
      avlnode.rightnode=avlnode.parent.leftnode
      avlnode.parent.leftnode.parent=avlnode
    else: #caso contrario se le asigna None
      avlnode.rightnode=None
    avlnode.parent.leftnode=avlnode
  else: #Caso en el que es la Raiz
    B.root=avlnode.rightnode
    avlnode.rightnode.parent=None
    avlnode.parent=avlnode.rightnode
    if avlnode.parent.leftnode!=None: #Caso en el que el hijo derecho tenia un hijo izquierdo
      avlnode.rightnode=avlnode.parent.leftnode
      avlnode.parent.leftnode.parent=avlnode
    else:
      avlnode.rightnode=None
    avlnode.parent.leftnode=avlnode
  return B

#Recurrencia para calcular el BalanceFactor de un Arbol
def BalanceFactor(currentNode,height):
  if currentNode.leftnode==None and currentNode.rightnode==None: #Si no tiene hijos el balanceFactor es 0
    currentNode.bf=0
    height=height+1
    return height
  else:
    if currentNode.leftnode!=None: #Devuelve la altura del hijo izquierdo
      heightLeft=BalanceFactor(currentNode.leftnode,height) 
    else:
      heightLeft=0
    if currentNode.rightnode!=None: #Devuelve la altura del hijo derecho
      heightRight=BalanceFactor(currentNode.rightnode,height)
    else:
      heightRight=0
    currentNode.bf=heightLeft - heightRight #Calcula el BalanceFactor del CurrentNode
    if heightLeft>heightRight: #Retorna la altura mas alta
      return heightLeft+1
    else:
      return heightRight+1
  
#Subprograma que calcular el BalanceFactor de un arbol 
def calculateBalance(AVLTree):
  if AVLTree.root==None:
    return None
  else:
    BalanceFactor(AVLTree.root,0)
    return AVLTree
    

#Subprograma recursivo que realiza el balanceo del arbol B en caso de necesitar realizar rotacion para balancearlo
def Balance(B,currentNode): 
  if currentNode.parent.bf>1: #Caso que el padre este inclinado hacia IZQUIERDA
    if currentNode.bf<0: #Caso que el nodo a rotar tenga inclinacion a DERECHA
      B=rotateLeft(B,currentNode)
      cambio=currentNode.bf
      currentNode.bf=currentNode.parent.bf*(-1)
      currentNode.parent.bf=cambio*(-1)
      currentNode=currentNode.parent
    B=rotateRight(B,currentNode.parent)
    currentNode.bf=currentNode.bf-1
    if currentNode.rightnode.leftnode==None and currentNode.rightnode.rightnode!=None: #Si el nuevo nodo padre NO tenia hijo derecho
      currentNode.rightnode.bf=currentNode.rightnode.bf-2
    elif currentNode.rightnode.leftnode!=None and currentNode.rightnode.rightnode==None: #Si el nuevo nodo padre tenia hijo derecho
      currentNode.rightnode.bf=currentNode.rightnode.bf-1
    else:
      currentNode.rightnode.bf=0
  elif currentNode.parent.bf<-1: #Caso que el padre este inclinado hacia DERECHA
    if currentNode.bf>0: #Caso que el nodo a rotar tenga inclinacion a IZQUIERDA
      B=rotateRight(B,currentNode)
      cambio=currentNode.bf
      currentNode.bf=currentNode.parent.bf*(-1)
      currentNode.parent.bf=cambio*(-1)
      currentNode=currentNode.parent
    B=rotateLeft(B,currentNode.parent)
    currentNode.bf=currentNode.bf+1
    if currentNode.leftnode.rightnode==None and currentNode.leftnode.leftnode!=None: #Si el nuevo nodo padre NO tenia hijo izquierdo
      currentNode.leftnode.bf=currentNode.leftnode.bf+2
    elif currentNode.leftnode.rightnode!=None and currentNode.leftnode.leftnode==None: #Si el nuevo nodo padre tenia hijo izquierdo
      currentNode.leftnode.bf=currentNode.leftnode.bf+1
    else:
      currentNode.leftnode.bf=0
        
def searchNoBalance(currentNode):
  if currentNode!=None:
    if currentNode.bf>1:
      return currentNode.leftnode
    elif currentNode.bf<-1:
      return currentNode.rightnode
    else:
      searchNoBalance(currentNode.leftnode)
      searchNoBalance(currentNode.rightnode)
    
   

def reBalance(AVLTree):
  if AVLTree==None:
    return None
  elif AVLTree.root==None:
    return None
  else:
    AVLTree=calculateBalance(AVLTree)
    Node=searchNoBalance(AVLTree.root)
    if Node!=None:
      Balance(AVLTree,Node)
  


#Parte recursiva del subprograma search
def searchTree(currentNode,element):
  if currentNode.value==element:
    return currentNode.key
  else:
    if currentNode.leftnode!=None:
      key=searchTree(currentNode.leftnode,element)
      if key!=None:
        return key
    if currentNode.rightnode!=None:
      key=searchTree(currentNode.rightnode,element)
      if key!=None:
        return key

#Subprograma que recibe un arbol binario y un elemento, devuelve la key del nodo donde se encuentra ese elemento, en caso de no encontrar dicho elemento devuelve None
def search(B,element):
  if B.root==None:
    return None
  else:
    return searchTree(B.root,element)

#Subprograma que busca el Menor de sus Mayores, desvinculandolo y devolviendo dicho nodo para ser reemplazado
def MenorDeMayores(currentNode):
  if currentNode.leftnode!=None:
    return MenorDeMayores(currentNode.leftnode)
  if currentNode.rightnode!=None:
    currentNode.parent.leftnode=currentNode.rightnode
    currentNode.rightnode.parent=currentNode.parent
  else:
    if currentNode.parent.key<currentNode.key:
      currentNode.parent.rightnode=None
    else:
      currentNode.parent.leftnode=None
  return currentNode

#Subprograma que es la parte recursiva a la hora de buscar el nodo a eliminar para el subprograma DELETE y DELETEKEY
def deleteNodeTree(B,currentNode,key):
  if currentNode.key==key:
    if currentNode.rightnode==None and currentNode.leftnode==None: #Caso que el nodo a eliminar no tenga hijos
      if currentNode.parent==None:
        B.root=None
      else:
        if currentNode.parent.key>key:
          currentNode.parent.leftnode=None
          currentNode.parent=None
        else:
          currentNode.parent.rightnode=None
          currentNode.parent=None
      return key
    elif currentNode.rightnode!=None and currentNode.leftnode==None: #Caso que el nodo a eliminar solo tenga hijo derecho
      if currentNode.parent==None:
        B.root=currentNode.rightnode
        B.root.parent=None
      else:
        if currentNode.parent.key>key:
          currentNode.parent.leftnode=currentNode.rightnode
          currentNode.rightnode.parent=currentNode.parent
          currentNode.parent=None
        else:
          currentNode.parent.rightnode=currentNode.rightnode
          currentNode.rightnode.parent=currentNode.parent
          currentNode.parent=None
      return key
    elif currentNode.rightnode==None and currentNode.leftnode!=None: #Caso que el nodo a eliminar solo tenga hijo izquierdo
      if currentNode.parent==None:
        B.root=currentNode.leftnode
        B.root.parent=None
      else:
        if currentNode.parent.key>key:
          currentNode.parent.leftnode=currentNode.leftnode
          currentNode.leftnode.parent=currentNode.parent
          currentNode.parent=None
        else:
          currentNode.parent.rightnode=currentNode.leftnode
          currentNode.leftnode.parent=currentNode.parent
          currentNode.parent=None
      return key
    elif currentNode.rightnode!=None and currentNode.leftnode!=None: #Caso que el nodo a eliminar tenga 2 hijos
      NewNode=MenorDeMayores(currentNode.rightnode)
      NewNode.rightnode=currentNode.rightnode
      if currentNode.rightnode!=None:
        currentNode.rightnode.parent=NewNode
      NewNode.leftnode=currentNode.leftnode
      if currentNode.leftnode!=None:
        currentNode.leftnode.parent=NewNode
      if currentNode.parent==None:
        NewNode.parent=currentNode.parent
        B.root=NewNode
        B.root.parent=None
      else:
        if currentNode.parent.key>key:
          currentNode.parent.leftnode=NewNode
          NewNode.parent=currentNode.parent
          currentNode.parent=None
        else:
          currentNode.parent.rightnode=NewNode
          NewNode.parent=currentNode.parent
          currentNode.parent=None
      return key

  elif currentNode.key>key:
    return deleteNodeTree(B,currentNode.leftnode,key)
  else:
    return deleteNodeTree(B,currentNode.rightnode,key)

#Subprograma que recibe un arbol binario y un elemento, elimina el nodo que contenga a dicho elemento y lo reemplaza por el Menor de su Mayores
def delete(B,element):
  key=search(B,element)
  if key!=None:
    deleteNodeTree(B,B.root,key)
    return reBalance(B)
  return None

#Subprograma que recibe un arbol binario y una key, elimina el nodo qu contenga a dicha key y lo reemplaza por el Menor de su Mayores
def deleteKey(B,key):
  return deleteNodeTree(B,B.root,key)

#Subprograma que realiza los cambios del Balance Factor y las rotaciones en caso de ser necesario
def BFchange(B,currentNode):
  if currentNode.parent!=None:
    if currentNode.parent.bf==0:
      if currentNode.parent.key>currentNode.key:
        currentNode.parent.bf=1
        BFchange(B,currentNode.parent)
      elif currentNode.parent.key<currentNode.key:
        currentNode.parent.bf=-1
        BFchange(B,currentNode.parent)
    elif currentNode.parent.bf==1:
      if currentNode.parent.key>currentNode.key:
        currentNode.parent.bf=2
        Balance(B,currentNode)
      elif currentNode.parent.key<currentNode.key:
        currentNode.parent.bf=0
        return
    else:
      if currentNode.parent.key>currentNode.key:
        currentNode.parent.bf=0
        return
      elif currentNode.parent.key<currentNode.key:
        currentNode.parent.bf=-2
        Balance(B,currentNode)
      

#Parte recursiva del subprograma insert
def insertTree(B,currentNode,NewNode):
  if currentNode.key<NewNode.key:
    if currentNode.rightnode==None:
      currentNode.rightnode=NewNode
      NewNode.parent=currentNode
      BFchange(B,NewNode)
      return NewNode.key
    else:
      return insertTree(B,currentNode.rightnode,NewNode)
  elif currentNode.key>NewNode.key:
    if currentNode.leftnode==None:
      currentNode.leftnode=NewNode
      NewNode.parent=currentNode
      BFchange(B,NewNode)
      return NewNode.key
    else:
      return insertTree(B,currentNode.leftnode,NewNode)

#Subprograma que recibe un arbol binario, un elemento y una key, se encarga de ingresar dicho nodo con el elemento y la key ingresada dentro del arbol binario, retorna la misma key si ha logrado ingresarse
def insert(B,element,key):
  if B.root==None:
    B.root=AVLNode()
    B.root.value=element
    B.root.key=key
    B.root.bf=0
    return key
  else:
    NewNode=AVLNode()
    NewNode.value=element
    NewNode.key=key
    NewNode.bf=0
    return insertTree(B,B.root,NewNode)

#Subprograma que es la parte recursiva del subprograma ACCESS
def accessTree(currentNode,key):
  if currentNode!=None:
    if currentNode.key==key:
      return currentNode.value
    elif currentNode.key>key:
      return accessTree(currentNode.leftnode,key)
    else:
      return accessTree(currentNode.rightnode,key)

#Subprograma que recibe un arbol binario y una key, devuelve el elemento que contenga dicha key, en caso de no existir devuelve None
def access(B,key):
  if B.root==None:
    return None
  else:
    return accessTree(B.root,key)

def updateTree(currentNode,element,key):
  if currentNode!=None:
    if currentNode.key==key:
      currentNode.value=element
      return currentNode.key
    elif currentNode.key>key:
      return accessTree(currentNode.leftnode,key)
    else:
      return accessTree(currentNode.rightnode,key)

def update(B,element,key):
  if access(B,key)!=None:
    return updateTree(B.root,element,key)


#Subprograma que es la parte recursiva del subprograma traverseInOrder
def inorder(currentNode,L):
  if currentNode.leftnode!=None:
    inorder(currentNode.leftnode,L)
  linkedlist.addTree(L,currentNode.value,currentNode.key)
  if currentNode.rightnode!=None:
    inorder(currentNode.rightnode,L)

#Subprograma que recibe un arbol y devuelve una LinkedList de los elementos INORDER
def traverseInOrder(B):
  if B.root==None:
    return None
  else:
    L=linkedlist.LinkedList()
    inorder(B.root,L)
    linkedlist.invertirlista(L)
    return L

#Subprograma que es la parte recursiva del subprograma traverseInPostOrder
def postorder(currentNode,L):
  if currentNode.leftnode!=None:
    postorder(currentNode.leftnode,L)
  if currentNode.rightnode!=None:
    postorder(currentNode.rightnode,L)
  linkedlist.addTree(L,currentNode.value,currentNode.key)

#Subprograma que recibe un arbol y devuelve una LinkedList de los elementos POSTORDER
def traverseInPostOrder(B):
  if B.root==None:
    return None
  else:
    L=linkedlist.LinkedList()
    postorder(B.root,L)
    linkedlist.invertirlista(L)
    return L

#Subprograma que es la parte recursiva del subprograma traverseInPreOrder
def preorder(currentNode,L):
  linkedlist.addTree(L,currentNode.value,currentNode.key)
  #print("ingrese con ",currentNode.value," y se guardo")
  #printlist(L)
  if currentNode.leftnode!=None:
    preorder(currentNode.leftnode,L)
  if currentNode.rightnode!=None:
    preorder(currentNode.rightnode,L)

#Subprograma que recibe un arbol y devuelve una LinkedList de los elementos PREORDER
def traverseInPreOrder(B):
  if B.root==None:
    return None
  else:
    L=linkedlist.LinkedList()
    preorder(B.root,L)
    linkedlist.invertirlista(L)
    return L

#Subprograma que recibe un arbol y devuelve una LinkedList de los elementos por AMPLITUD
def traverseBreadFirst(B):
  queue=linkedlist.LinkedList()
  queueList=linkedlist.LinkedList()
  linkedlist.add(queue,B.root)
  while queue.head!=None:
    currentNode=dequeue(queue)
    linkedlist.add(queueList,currentNode.value)
    if currentNode.leftnode!=None:
      linkedlist.add(queue,currentNode.leftnode)
    if currentNode.rightnode!=None:
      linkedlist.add(queue,currentNode.rightnode)
  linkedlist.invertirlista(queueList)
  return queueList