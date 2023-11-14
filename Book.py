class Book:
    def __init__(self, BookId=0, BookName="", AuthorName="", AvailabilityStatus=True, BorrowedBy=None):
        self.BookId = int(BookId)
        self.BookName = BookName 
        self.AuthorName = AuthorName
        self.AvailabilityStatus = AvailabilityStatus
        self.BorrowedBy = BorrowedBy
        self.ReservationHeap = []

    def __str__(self):
        return f"BookID = {self.BookId}\nTitle = \"{self.BookName}\"\nAuthor = \"{self.AuthorName}\"\n" \
               f"Availability = \"{'Yes' if self.AvailabilityStatus else 'No'}\"\n" \
               f"BorrowedBy = {self.BorrowedBy if self.AvailabilityStatus is False else 'None'}\n" \
               f"Reservations = {self.get_reservation_list()}\n\n"

    def get_reservation_list(self):
        return [reservation[0] for reservation in self.ReservationHeap]

    def add_reservation(self, patron_id, priority_number, time_of_reservation):
        reservation = (patron_id, priority_number, time_of_reservation)
        self.ReservationHeap.append(reservation)
        self._heapify_up()

    def _heapify_up(self):
        index = len(self.ReservationHeap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self._compare_reservations(index, parent_index) < 0:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _compare_reservations(self, index1, index2):
        # Compare reservations based on priority and timestamp
        patron_id1, priority_number1, time_of_reservation1 = self.ReservationHeap[index1]
        patron_id2, priority_number2, time_of_reservation2 = self.ReservationHeap[index2]

        if priority_number1 < priority_number2 or (priority_number1 == priority_number2 and time_of_reservation1 < time_of_reservation2):
            return -1
        elif priority_number1 > priority_number2 or (priority_number1 == priority_number2 and time_of_reservation1 > time_of_reservation2):
            return 1
        else:
            return 0

    def _swap(self, index1, index2):
        # Swap two reservations in the heap
        self.ReservationHeap[index1], self.ReservationHeap[index2] = self.ReservationHeap[index2], self.ReservationHeap[index1]