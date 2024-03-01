class Book:
    # Dunder Methods
    def __init__(self, BookId=0, BookName="", AuthorName="", AvailabilityStatus=True, BorrowedBy=None):
        self.BookId = int(BookId)
        self.BookName = BookName 
        self.AuthorName = AuthorName
        self.AvailabilityStatus = AvailabilityStatus
        self.BorrowedBy = BorrowedBy
        self.ReservationHeap = []

    def __str__(self):
        return f"BookID = {str(self.BookId).strip()}\nTitle = \"{self.BookName.strip()}\"\nAuthor = \"{self.AuthorName.strip()}\"\n" \
               f"Availability = \"{'Yes' if self.AvailabilityStatus else 'No'}\"\n" \
               f"BorrowedBy = {self.BorrowedBy if self.AvailabilityStatus is False else 'None'}\n" \
               f"Reservations = {self.get_reservation_list()}\n\n"
        
    # Inner Class
    class Reservation:
        # Instance Methods
        def __init__(self,patron_id, priority_number, time_of_reservation):
            self.patron_id = patron_id
            self.priority_number = priority_number
            self.time_of_reservation = time_of_reservation

        # Dunder Methods
        def __lt__(self,other):
            return self.priority_number < other.priority_number or (self.priority_number == other.priority_number and self.time_of_reservation > other.time_of_reservation)
        
        def __gt__(self,other):
            return self.priority_number > other.priority_number or (self.priority_number == other.priority_number and self.time_of_reservation < other.time_of_reservation)
        
        def __str__(self):
            return str(self.patron_id)

    # Instance Methods
    def get_reservation_list(self):
        return [reservation.patron_id for reservation in sorted(self.ReservationHeap, key=lambda reservation: (reservation.priority_number, reservation.time_of_reservation))]

    def add_reservation(self, patron_id, priority_number, time_of_reservation):
        reservation = Book.Reservation(patron_id, priority_number, time_of_reservation)
        # self.ReservationHeap.append(reservation)
        self.insert_min_heap(reservation)

    def insert_min_heap(self,reservation):
        heap = self.ReservationHeap
        heap.append(reservation)
        index = len(heap) - 1
        while index > 0 and heap[(index - 1) // 2] > heap[index]:
            heap[index], heap[(index - 1) //2] = heap[(index - 1) // 2], heap[index]
            index = (index - 1) // 2
