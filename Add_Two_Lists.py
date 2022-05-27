class Node: 
    def __init__ (self,data):
        self.data = data
        self.next_node = None

class LList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node
    
    def __str__(self):
        output = ""
        temp = self.head
        while temp != None:
            output += str(temp.data)
            if temp.next_node != None:
                output += " -> "
            temp  = temp.next_node
        return output

def addTwoList(list1,list2):
    added = 0
    spot = 1
    temp1 = list1.head
    temp2 = list2.head
    while temp1 != None or temp2 != None:
        if temp1 != None and temp2 != None:
            added += (temp1.data * spot)
            added += (temp2.data * spot)
            spot = spot * 10
            temp1 = temp1.next_node
            temp2 = temp2.next_node
        elif temp1 != None and temp2 == None:
            added += temp1.data * spot
            spot = spot * 10
            temp1 = temp1.next_node
        elif temp1 == None and temp2 != None:
            added += temp2.data * spot
            spot = spot * 10
            temp1 = temp2.next_node
    final = LList()
    for i in str(added):
        final.push(int(i))
    return final

if __name__ == "__main__":
    one1 = LList()
    two2 = LList()
    set1 = input("Please input number for first list: ")
    set2 = input("Please input number for second list: ")
    for i in str(set1):
        one1.push(int(i))
    for i in str(set2):
        two2.push(int(i))
    print(one1)
    print(two2)
    print(addTwoList(one1,two2))