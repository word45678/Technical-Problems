class Node: #this builds the Node class that will make up each part of our linked list
    def __init__ (self,data): #this constructs each node using itself and an input of data to label the node with
        self.data = data #this sets the data of the node being built to the data argument given when a new instance of the class is made
        self.next_node = None #this by default sets the node this node is linked to to NULL, this will be changed later as data is pushed to the linked list in new nodes

class LList:
    def __init__(self): #this builds the linked list, it doesn't need anything to be built by default as we use a separate method "push" to add data to the list
        self.head = None #this sets the beginning of the list to NULL, but also creates the data space for the beginning of the list, which will be a node, which will be linked to the next node or to NONE, thus being a linked list

    def push(self, value): #this method is how we will add new data to the linked list, requiring an argument for the data to be added but not of a defined type, could be ints, strings, anything
        new_node = Node(value) #this creates a node object that we can link onto the head of the linked list, as a queue the linked list is first in first out, so any new items can just be appended to the end
        new_node.next_node = self.head #this sets the linked next object to our new node to the head of our linked list, this is half of the job of adding it to the list, it is now effectively the head of the list, we just need to tell the actual list that it is now the head of the list
        self.head = new_node #this is the other half of making this new data the head of the list, it tells the list object that this new node is now the actual head of the list
    
    def __str__(self): #this makes it easy for us to print the list by simply calling print(list), this function essentially tells the object what to return when the program calls for a string representation
        output = "" #this is where we'll put all of the elements in the list to actually be printed, making it easy for us to return after we iterate through the list
        temp = self.head #this gives us an extra space to iterate through the list, initialized as the head of the list
        while temp != None: #this allows us to use the extra space 'temp' to iterate through the list without actually affecting the list and stops it when 'temp' points to the end of the list
            output += str(temp.data) #this appends the data stored in the currently iterated node to our output text string
            output += " -> " #this makes a nice little arrow between the elements of the list
            temp  = temp.next_node #this is actually the next step in the iteration, pushing our 'temp' pointer further down the list
        return output #this returns our concatenated string of all of the data found in the linked list
    
    def reverse(self): #this is the function that will reverse the list, this will act on the list rather than return a new reversed list
        current = self.head #this is a pointer to follow through the list, starting at the beginning
        prev = None #this is another pointer to follow through the list, starting BEFORE the beginning
        while current != None: #this iterated our pointer through the list until it reaches the end
            temp = current.next_node #this is another pointer, set to the node in the list coming after the currently iterating one
            current.next_node = prev #this links the currently iterating node to the node before it, thus reversing its orientation in the list
            prev = current #this sets our "one before" pointer to the next node, thus allowing it to keep up with the iterations
            current = temp #this sets our currently iterating node to the next node in the list, or NULL if at the end
        self.head = prev #and this sets the node just before NULL at the end of the list to the new head of the list
        #imagine if you will a set of dominoes, each node is a domino and the act of falling over is the orientation of the domino going from -> to <-, and that's essentially our process, where after all of the dominoes have fallen we just proclaim to the world "that last domino is actually the first domino now!" and thus the list is reversed

data = input("Please enter a comma separated list of data: ")
data = data.split(",")#this reads the user input into a list of items we can iterate through and push to the linked list
foo = LList() #these lists work with any data in any combination, it's great
for i in range(len(data)): #we can't just push the whole list at once, because then the list will be added as the data on one node, not separate nodes, more functionality coming soon :)
    foo.push(data[i])
print(foo) #remember that __str__ function we made earlier? isn't this convenient?
foo.reverse()
print(foo)

