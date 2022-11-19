from data import *
from seat import *

class node:
    def __init__(self, data): #Final       
        self.data = data
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.prev = None
        self.next = None


class Two_Dimensional_Double_Linked_List:

    def __init__(self,row = 0,col = 0): #subject to change
        self.head = None
        self.head_down = None
        self.mainhead = None
        self.head_temp = None
        self.rows = row
        self.columns = col
        self.index = 0
        self.hold = None
        self.list = []
        self.length_list = 0
        self.columns_index = []
    
    def prepend(self, new_data): #Final
        self.append_left(self.hold)
        new_node_2D = node(new_data)
        for i in range(self.columns):
            self.append_left(new_data[-i-1])
        new_node_2D.next = self.mainhead

        if self.mainhead is not None:
	        self.mainhead.prev = new_node_2D
        
        self.mainhead = new_node_2D
        self.rows += 1

    def append_2D(self,new_data): #Final
        new_node_2D = node(new_data)
        
        for i in range(self.columns):
            self.append_right(new_data[i])
        #if type(new_data) == list or type(new_data) == pd.core.frame.DataFrame:
        self.append_right(self.hold)
        

        if self.mainhead is None:
            self.mainhead = new_node_2D
            return

        last = self.mainhead
        while last.next:
            last = last.next
        last.next = new_node_2D
        new_node_2D.prev = last
        self.rows += 1
        return

    def append_right(self,new_data): #Final
        new_node_right = node(new_data)

        if self.head is None:
            self.head = new_node_right
            return
        last = self.head
        while last.right:
            last = last.right
        last.right = new_node_right
        new_node_right.left = last
        return
    
    def append_left(self,new_data): #Final
        new_node = node(new_data)
        new_node.right = self.head
        if self.head is not None:  
            self.head.left = new_node
        self.head = new_node

    def delete_data_node(self,dele): #Final
		# Base Case
        if self.head is None or dele is None:
	        return
		
		# If node to be deleted is head node
        if self.head == dele:
            self.head = dele.right

		# Change next only if node to be deleted is NOT
		# the last node
        if dele.right is not None:
            dele.right.left = dele.left
	
		# Change prev only if node to be deleted is NOT
		# the first node
        if dele.left is not None:
            dele.left.right = dele.right

    def printList(self, node): #subject to change

        print("\nTraversal in forward direction")
        #while node:
        #for i in range(3):
        #    node = node.down
        for i in range(self.rows+1):
            self.list = []
            for j in range(self.columns+1):
                if i == 0:
                    if j == 0:
                        self.list.append(node.data)
                        #print(node.data,end = "")
                    else:
                        node = node.right
                        self.list.append(node.data)
                else:
                    node = node.right
                    self.list.append(node.data)

                #print(node.data,end = "")
            print(self.list)
    
    def add_column_index(self,data): #Final
        self.columns_index = data
        return self.columns_index

    def return_column(self,column_name,node): #Final
        data_out = []
        node_count = 0
        all_count  = 0
        if column_name in self.columns_index:
            self.index = 0

            for i in range(self.columns):
                if column_name == self.columns_index[i]:
                    self.index = i

            while node_count < self.index:
                node = node.right
                node_count += 1
            data_out.append(node.data)
            node_count = 0

            while all_count < self.rows:
                while node_count < self.columns+1:
                    node = node.right
                    node_count += 1
                data_out.append(node.data)
                all_count +=1
                node_count = 0
        else:
            print("Error Column name")
        
        return data_out
    
    def delete_data(self, dele): #Final
		
		# Base Case
        if self.mainhead is None or dele is None:
	        return
		
		# If node to be deleted is head node
        if self.mainhead == dele:
            self.mainhead = dele.next

		# Change next only if node to be deleted is NOT
		# the last node
        if dele.next is not None:
            dele.next.prev = dele.prev
	
		# Change prev only if node to be deleted is NOT
		# the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        
        for i in range(self.columns):
            self.delete_data_node(dele)

        self.rows -= 1

    def length(self): #Final
        for i in range(self.rows+1):
            for j in range(self.columns+1):
                self.length_list += 1
        return self.length_list

    def datatype(self): #subject to change
        counter = 0
        while node != None:
            if type(node) == str:
                counter += 1
                
            node = node.right
                
        #print("\nTraversal in reverse direction")
        #while last:
        #    print(" {}".format(last.data))
        #   last = last.left
 
