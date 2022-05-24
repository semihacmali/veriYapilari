class Node():
    #data // veriyi tutacak
    #nextNode // sonraki node'u gösterecek
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
    def getData(self):
        return self.data
    
    def getNextNode(self):
        return self.nextNode
    
    def setData(self, data):
        self.data = data
    
    def setNextNode(self, nextNode):
        self.nextNode = nextNode

def printLinkedList(root):
    tmp = root
    if root == None:
        print("Linked List is Empty!")
    else:
        while tmp.getNextNode():
            print(tmp.getData())
            tmp = tmp.getNextNode()
        print(tmp.getData())

## kucukten buyuge sirali ekleme olarak guncellenecek
def addNode(root, newNode):
    tmp = root
    if root == None:
        tmp = newNode
    while tmp.getNextNode():
       tmp = tmp.getNextNode()
    tmp.setNextNode(newNode)
    return root

def delRear(root):
    tmp = root
    if root == None:
        tmp = "Linked List is Empty!"
    elif tmp.getNextNode() == None:
        root = None
    else:
        while tmp.getNextNode().getNextNode() is not None: # en sondaki elemanı silmek icin en sondan bir onceye kadar gitmem lazim
            tmp = tmp.getNextNode()
        tmp.setNextNode(None)
    return root

def delFront(root):
    if root == None:
        root = "Linked List is Empty!"
    elif root.getNextNode() == None:
        root = None
    else:
        root = root.getNextNode()
    return root

root = Node(5)        
root = addNode(root, Node(9))
printLinkedList(root)
root = delFront(root)
printLinkedList(root)
root = addNode(root, Node(11))
printLinkedList(root)
root = addNode(root, Node(13))
printLinkedList(root)
root = delRear(root)
printLinkedList(root)
root = delRear(root)
printLinkedList(root)
root = delRear(root)
printLinkedList(root)
root = delRear(root)
printLinkedList(root)

root = Node(5)        
root = addNode(root, Node(9)) # 5 , 9
       
root = addNode(root, Node(3)) # 3 ,5 , 9 
        
root = addNode(root, Node(7)) # 3 , 5 , 7 ,9
       
root = addNode(root, Node(11))# 3 , 5, 7, 9, 11
