class Book:
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
        
    class Reservation:
        def __init__(self,patron_id, priority_number, time_of_reservation):
            self.patron_id = patron_id
            self.priority_number = priority_number
            self.time_of_reservation = time_of_reservation

        def __lt__(self,other):
            return self.priority_number < other.priority_number or (self.priority_number == other.priority_number and self.time_of_reservation > other.time_of_reservation)
        
        def __gt__(self,other):
            return self.priority_number > other.priority_number or (self.priority_number == other.priority_number and self.time_of_reservation < other.time_of_reservation)
        
        def __str__(self):
            return str(self.patron_id)

    def get_reservation_list(self):
        return [reservation.patron_id for reservation in sorted(self.ReservationHeap, key=lambda reservation: (reservation.priority_number, reservation.time_of_reservation))]


    def add_reservation(self, patron_id, priority_number, time_of_reservation):
        reservation = Book.Reservation(patron_id, priority_number, time_of_reservation)
        # self.ReservationHeap.append(reservation)
        self.insert_min_heap(reservation)

    # def _heapify_up(self):
    #     index = len(self.ReservationHeap) - 1
    #     while index > 0:
    #         parent_index = (index - 1) // 2
    #         if self._compare_reservations(index, parent_index) < 0:
    #             self._swap(index, parent_index)
    #             index = parent_index
    #         else:
    #             break

    # def _compare_reservations(self, index1, index2):
    #     # Compare reservations based on priority and timestamp
    #     patron_id1, priority_number1, time_of_reservation1 = self.ReservationHeap[index1]
    #     patron_id2, priority_number2, time_of_reservation2 = self.ReservationHeap[index2]

    #     if priority_number1 < priority_number2 or (priority_number1 == priority_number2 and time_of_reservation1 > time_of_reservation2):
    #         return -1
    #     elif priority_number1 > priority_number2 or (priority_number1 == priority_number2 and time_of_reservation1 < time_of_reservation2):
    #         return 1
    #     else:
    #         return 0

    def _swap(self, index1, index2):
        # Swap two reservations in the heap
        self.ReservationHeap[index1], self.ReservationHeap[index2] = self.ReservationHeap[index2], self.ReservationHeap[index1]

    def insert_min_heap(self,reservation):
        heap = self.ReservationHeap
        heap.append(reservation)
        index = len(heap) - 1
        while index > 0 and heap[(index - 1) // 2] > heap[index]:
            heap[index], heap[(index - 1) //2] = heap[(index - 1) // 2], heap[index]
            index = (index - 1) // 2
    
    def print_min_heap_sorted(self):
        heap = self.ReservationHeap
        heap_copy = heap.copy()  # Create a copy to avoid modifying the original heap
        sorted_list = []

        while heap_copy:
            sorted_list.append(heap_copy[0])  # Append the root (minimum) element to the sorted list
            last = heap_copy.pop()  # Remove the last element

            if heap_copy:
                heap_copy[0] = last  # Place the last element at the root
                # Heapify the modified heap to maintain the min heap property
                current = 0
                while True:
                    smallest = current
                    left = 2 * current + 1
                    right = 2 * current + 2

                    if left < len(heap_copy) and heap_copy[left] < heap_copy[smallest]:
                        smallest = left

                    if right < len(heap_copy) and heap_copy[right] < heap_copy[smallest]:
                        smallest = right

                    if smallest == current:
                        break

                    heap_copy[current], heap_copy[smallest] = heap_copy[smallest], heap_copy[current]
                    current = smallest
        return sorted_list

