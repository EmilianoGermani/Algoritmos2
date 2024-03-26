
from linkedlist import *

def enqueue(Q,element):
  add(Q,element)

def dequeue(Q):
  if Q.head==None:
    return None
  elif length(Q)==1:
    element=Q.head.value
    Q.head=None
    return element
  else:
    currentNode=Q.head
    while currentNode.nextNode.nextNode!=None:
      currentNode=currentNode.nextNode
    element=currentNode.nextNode.value
    currentNode.nextNode=None
    return element