import time
# Importing the Book class from a module named Book
from Book import Book 

# Class representing a node in the Red-Black Tree
class RBTreeNode:  
    def __init__(self, book):  # Constructor for RBTreeNode
        self.book = book  # Holds a book object
        self.color = "RED"  # Node color initialized as RED
        self.left = None  # Left child initialized as None
        self.right = None  # Right child initialized as None
        self.parent = None  # Parent node initialized as None
        self.colorChangingFunctionId = 0  # Id to track color changes

# Class representing the Red-Black Tree
class RedBlackTree:  
    # Constructor for RedBlackTree
    def __init__(self):  
        self.NULL = RBTreeNode(Book())  # Creating a NULL node with a default book object
        self.NULL.color = "BLACK"  # NULL node color set as BLACK
        self.NULL.left = None  # Initializing left child of NULL node as None
        self.NULL.right = None  # Initializing right child of NULL node as None
        self.root = self.NULL  # Initializing root of the tree as NULL
        self.color_flip_count = 0  # Counter to track color changes
        self.currentFunctionId = 0  # Identifier to track function calls

    def LeftRotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def RightRotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def Insert(self, z):
        
        z.parent = None
        z.left = self.NULL
        z.right = self.NULL
        z.color = "RED"    

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if z.book.BookId < x.book.BookId:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y is None:
            self.root = z
        elif z.book.BookId < y.book.BookId:
            y.left = z
        else:
            y.right = z

        if z.parent is None:                         # Root node is always Black
            z.color = "BLACK"
            return
        
        if z.parent.parent is None :                  # If parent of node is Root Node
            return
        
        self.InsertFixup(z)

    def InsertFixup(self, z):
        while z.parent.color == "RED":                     # While parent is red
            if z.parent == z.parent.parent.right:          # if parent is right child of its parent
                lg = z.parent.parent.left                  # Left child of grandparent
                if lg.color == "RED":                      # if color of left child of grandparent i.e, uncle node is red
                    self.ChangeNodeColor(lg,"BLACK")       # Set both children of grandparent node as black 
                    self.ChangeNodeColor(z.parent,"BLACK")
                    self.ChangeNodeColor(z.parent.parent,"RED") # Set grandparent node as Red                    
                    z = z.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if z == z.parent.left:                # If k is left child of it's parent
                        z = z.parent
                        self.RightRotate(z)                        # Call for right rotation

                    self.ChangeNodeColor(z.parent,"BLACK")
                    self.ChangeNodeColor(z.parent.parent,"RED")
                    self.LeftRotate(z.parent.parent)
            else:       
                rg = z.parent.parent.right                      # Right child of grandparent
                if rg.color == 'RED':                           # if color of right child of grandparent i.e, uncle node is red
                    self.ChangeNodeColor(rg,"BLACK")            # Set color of childs as black
                    self.ChangeNodeColor(z.parent,"BLACK")
                    self.ChangeNodeColor(z.parent.parent,"RED") # set color of grandparent as Red
                    z = z.parent.parent                         # Repeat algo on grandparent to remove conflicts
                else:
                    if z == z.parent.right:                     # if k is right child of its parent
                        z = z.parent
                        self.LeftRotate(z)                       # Call left rotate on parent of k                   
                    self.ChangeNodeColor(z.parent,"BLACK")
                    self.ChangeNodeColor(z.parent.parent,"RED")
                    self.RightRotate(z.parent.parent)             # Call right rotate on grandparent
            if z == self.root:                                    # If k reaches root then break
                break
        
        self.ChangeNodeColor(self.root,"BLACK")                    # Set color of root as black
                               
        
    def Transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def DeleteFixup(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:   # If x is left child of parent 
                w = x.parent.right
                if w.color == "RED":
                    self.ChangeNodeColor(w,"BLACK")
                    self.ChangeNodeColor(x.parent,"RED")
                    self.LeftRotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    self.ChangeNodeColor(w,"RED")
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        self.ChangeNodeColor(w,"BLACK")
                        self.ChangeNodeColor(w,"RED")
                        self.RightRotate(w)
                        w = x.parent.right
                    self.ChangeNodeColor(w,x.parent.color)
                    self.ChangeNodeColor(x.parent,"BLACK")
                    self.ChangeNodeColor(w.right,"BLACK")
                    self.LeftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    self.ChangeNodeColor(w.color,"BLACK")
                    self.ChangeNodeColor(x.parent,"RED")
                    self.RightRotate(x.parent)
                    w = x.parent.left

                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    self.ChangeNodeColor(w,"RED")
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        self.ChangeNodeColor(w.right,"BLACK")
                        self.ChangeNodeColor(w,"RED")
                        self.LeftRotate(w)
                        w = x.parent.left
                    self.ChangeNodeColor(w,x.parent.color)
                    self.ChangeNodeColor(x.parent,"BLACK")
                    self.ChangeNodeColor(w.left,"BLACK")
                    self.RightRotate(x.parent)
                    x = self.root

        self.ChangeNodeColor(x,"BLACK")

    def Delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.Transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.Transplant(z, z.left)
        else:
            y = self.TreeMaximum(z.left)
            y_original_color = y.color
            x = y.left
            if y.parent == z:
                x.parent = y
            else:
                self.Transplant(y, y.left)
                y.left = z.left
                y.left.parent = y

            self.Transplant(z, y)
            y.right = z.right
            y.right.parent = y
            self.ChangeNodeColor(y, z.color)

        if y_original_color == "BLACK":
            self.DeleteFixup(x)

    def TreeMaximum(self, x):
        while x.right != self.NULL:
            x = x.right
        return x

    def InsertBook(self, book_id, book_name, author_name, availability_status=True, borrowed_by=None, reservation_heap=None):
        book = Book(book_id, book_name, author_name, availability_status, borrowed_by)
        z = RBTreeNode(book)
        self.currentFunctionId+=1
        self.Insert(z)
        return ""

    def DeleteBook(self, book_id):
        z = self.SearchBookNode(self.root, book_id)
        reservation = [str(x) for x in z.book.get_reservation_list()]
        if z is not None and z.book.BookId !=0:
            self.currentFunctionId+=1
            self.Delete(z)
            if len(reservation)>1:
                return f"Book {book_id} is no longer available. Reservations made by Patrons {', '.join(reservation)} have been cancelled!\n\n"
            elif len(reservation)==1:
                return f"Book {book_id} is no longer available. Reservation made by Patron {reservation[0]} has been cancelled!\n\n"
            else:
                return f"Book {book_id} is no longer available.\n\n"
        else:
            return f"Book {book_id} not found in the Library\n\n"

    def SearchBookNode(self, node, book_id):
        while node != self.NULL and int(book_id) != int(node.book.BookId):
            if int(book_id) < int(node.book.BookId):
                node = node.left
            else:
                node = node.right
        return node

    def PrintBook(self, book_id):
        node = self.SearchBookNode(self.root, book_id)
        if (node is not None) and (node.book.BookId != 0):
            return str(node.book)
        else:
            return f"Book {book_id} not found in the Library\n\n"

    def PrintBooks(self, book_id1, book_id2):
        books = self.GetBooksInRange(self.root, book_id1, book_id2)
        opstring= ""
        if books:
            for book in books:
                opstring+=str(book)
        else:
            opstring ="No Books found in the given range."
        return opstring

    def GetBooksInRange(self, node, book_id1, book_id2):
        books = []
        if node is not None:
            if int(book_id1) < int(node.book.BookId):
                books.extend(self.GetBooksInRange(node.left, book_id1, book_id2))
            if int(book_id1) <= int(node.book.BookId) <= int(book_id2):
                books.append(node.book)
            if int(book_id2) > node.book.BookId:
                books.extend(self.GetBooksInRange(node.right, book_id1, book_id2))
        return books

    def BorrowBook(self, patron_id, book_id, patron_priority):
        book_node = self.SearchBookNode(self.root, book_id)
        if book_node is not None:
            if book_node.book.AvailabilityStatus:
                book_node.book.AvailabilityStatus = False
                book_node.book.BorrowedBy = patron_id
                return f"Book{book_id} Borrowed by Patron {patron_id}\n\n"
            else:
                book_node.book.add_reservation(int(patron_id), int(patron_priority), time.time())
                return f"Book{book_id} Reserved by Patron {patron_id}\n\n"
        else:
            return f"Book {book_id} not found in the Library\n\n"

    def ReturnBook(self, patron_id, book_id):
        book_node = self.SearchBookNode(self.root, book_id)
        if book_node is not None and not book_node.book.AvailabilityStatus:
            book_node.book.AvailabilityStatus = True
            book_node.book.BorrowedBy = None
            opmssg=f"Book{book_id} Returned by Patron {patron_id}\n\n"
            if book_node.book.ReservationHeap:
                reservation = book_node.book.ReservationHeap.pop(0)
                book_node.book.BorrowedBy = str(reservation)
                opmssg += f"Book{book_id} Allotted to Patron {reservation}\n\n"
                book_node.book.AvailabilityStatus = False
            return opmssg
        else:
            return f"Book{book_id} not found in the Library or not borrowed by Patron {patron_id}\n\n"

    def FindClosestBook(self, target_id):
        closest_nodes = self.FindClosestBookHelper(self.root, target_id)
        if closest_nodes:
            return "".join([str(book) for book in closest_nodes])
        else:
            return "No books in the Library.\n\n"

    def FindClosestBookHelper(self, node, target_id):
        if node is not None:
            closest_nodes = []
            # Traverse the tree to find the closest nodes
            while node:
                if int(node.book.BookId) == int(target_id):
                    return [node.book]

                if int(node.book.BookId) < int(target_id):
                    closest_nodes.append(node.book)
                    node = node.right
                else:
                    closest_nodes.append(node.book)
                    node = node.left

            # Find the inorder predecessor and successor
            pred, succ = self.InorderPredecessorSuccessor(target_id)

            # Calculate distances to the target ID
            pred_distance = abs(int(pred.book.BookId) - int(target_id)) if pred else float('inf')
            succ_distance = abs(int(succ.book.BookId) - int(target_id)) if succ else float('inf')

            # Compare distances and return the closest nodes
            if pred_distance < succ_distance:
                return [pred.book] if pred else []
            elif succ_distance < pred_distance:
                return [succ.book] if succ else []
            else:
                return sorted([pred.book, succ.book], key=lambda book: int(book.BookId) if book else float('inf'))
        return []

    def InorderPredecessorSuccessor(self, target_id):
        pred = None
        succ = None
        current = self.root

        while current.book.BookId !=0:
            if int(current.book.BookId) == int(target_id):
                if current.left:
                    pred = current.left
                    while pred.right:
                        pred = pred.right

                if current.right:
                    succ = current.right
                    while succ.left:
                        succ = succ.left

                break
            elif int(current.book.BookId) < int(target_id):
                pred = current
                current = current.right
            else:
                succ = current
                current = current.left

        return pred, succ

    def ColorFlipCount(self):
        return f"Color Flip Count: {self.color_flip_count}\n\n"
    
    def ChangeNodeColor(self, node, new_color):
        if node.color != new_color:
            if node.colorChangingFunctionId != self.currentFunctionId:
                print(node.book.BookId, node.color,"-->", new_color, " +1")
                self.color_flip_count += 1  # Increment color flip count
                node.colorChangingFunctionId = self.currentFunctionId
            else:
                print(node.book.BookId, node.color,"-->", new_color, " -1")
                self.color_flip_count -= 1 
                node.colorChangingFunctionId = 0

        node.color = new_color
    
    def Quit(self):
        return "Program Terminated!!"
