import time
from Book import Book

class RBTreeNode:
    def __init__(self, book):
        self.book = book
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL = RBTreeNode(Book())
        self.NULL.color = "BLACK"
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.color_flip_count = 0

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

    def Insert(self, book):
        z = RBTreeNode(book)
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
        while z.parent.color == "RED":                        # While parent is red
            if z.parent == z.parent.parent.right:         # if parent is right child of its parent
                lg = z.parent.parent.left                  # Left child of grandparent
                if lg.color == "RED":                          # if color of left child of grandparent i.e, uncle node is red
                    lg.color = "BLACK"                           # Set both children of grandparent node as black
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"             # Set grandparent node as Red
                    z = z.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if z == z.parent.left:                # If k is left child of it's parent
                        z = z.parent
                        self.RightRotate(z)                        # Call for right rotation
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.LeftRotate(z.parent.parent)
            else:                                         # if parent is left child of its parent
                rg = z.parent.parent.right                 # Right child of grandparent
                if rg.color == 'Red':                          # if color of right child of grandparent i.e, uncle node is red
                    rg.color = "BLACK"                           # Set color of childs as black
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"             # set color of grandparent as Red
                    z = z.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if z == z.parent.right:               # if k is right child of its parent
                        z = z.parent
                        self.LeftRotate(z)                        # Call left rotate on parent of k
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.RightRotate(z.parent.parent)              # Call right rotate on grandparent
            if z == self.root:                            # If k reaches root then break
                break
        self.root.color = "BLACK"                               # Set color of root as black
        
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
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.LeftRotate(x.parent)
                    w = x.parent.right

                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.RightRotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.LeftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.RightRotate(x.parent)
                    w = x.parent.left

                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.LeftRotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.RightRotate(x.parent)
                    x = self.root

        x.color = "BLACK"

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
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.Transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.Transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.DeleteFixup(x)

    def TreeMinimum(self, x):
        while x.left != self.NULL:
            x = x.left
        return x

    def InsertBook(self, book_id, book_name, author_name, availability_status=True, borrowed_by=None, reservation_heap=None):
        book = Book(book_id, book_name, author_name, availability_status, borrowed_by)
        self.Insert(book)
        print("Inserting Book")
        print(book)
        return ""

    def DeleteBook(self, book_id):
        z = self.SearchBookNode(self.root, book_id)
        reservation = z.book.get_reservation_list()
        if z is not None:
            self.Delete(z)
            return f"Book {book_id} is no longer available. Reservations made by Patrons {', '.join(reservation)} have been cancelled!\n\n"
        else:
            print(f"Book {book_id} not found in the Library\n\n")

    def SearchBookNode(self, node, book_id):
        print(f"Srarching Node with id: {book_id}")
        print("Starting with node")
        print(node.book)
        while node != self.NULL and int(book_id) != int(node.book.BookId):
            if int(book_id) < int(node.book.BookId):
                print("Searching Left")
                node = node.left
            else:
                print("Searching Right")
                node = node.right
        return node

    def PrintBook(self, book_id):
        node = self.SearchBookNode(self.root, book_id)
        if node is not None:
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
            opstring ="No books found in the given range."
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
                return f"Book {book_id} borrowed by Patron {patron_id}\n\n"
            else:
                book_node.book.add_reservation(patron_id, patron_priority, time.time())
                return f"Book {book_id} reserved by Patron {patron_id}\n\n"
        else:
            return f"Book {book_id} not found in the Library\n\n"

    def ReturnBook(self, patron_id, book_id):
        book_node = self.SearchBookNode(self.root, book_id)
        if book_node is not None and not book_node.book.AvailabilityStatus:
            book_node.book.AvailabilityStatus = True
            book_node.book.BorrowedBy = None
            opmssg=f"Book {book_id} Returned by Patron {patron_id}\n\n"
            if book_node.book.ReservationHeap:
                reservation = book_node.book.ReservationHeap.pop(0)
                book_node.book.BorrowedBy = reservation[0]
                opmssg += f"Book {book_id} Allotted to Patron {reservation[0]}\n\n"
            return opmssg
        else:
            return f"Book {book_id} not found in the Library or not borrowed by Patron {patron_id}\n\n"

    def FindClosestBook(self, target_id):
        print(f"Find Closest for {target_id}")
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
            print(pred.book)
            print(succ.book)

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
        print(f"Color Flip Count: {self.color_flip_count}" )
        return f"Color Flip Count: {self.color_flip_count}\n\n"
    
    def Quit(self):
        return "Program Terminated!!"
