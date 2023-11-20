def insert_min_heap(heap, value):
	heap.append(value)
	index = len(heap) - 1
	while index > 0 and heap[(index - 1) // 2] > heap[index]:
		heap[index], heap[(index - 1) //2] = heap[(index - 1) // 2], heap[index]
		index = (index - 1) // 2


def delete_min_heap(heap, value):
	index = -1
	for i in range(len(heap)):
		if heap[i] == value:
			index = i
			break
	if index == -1:
		return
	heap[index] = heap[-1]
	heap.pop()
	while True:
		left_child = 2 * index + 1
		right_child = 2 * index + 2
		smallest = index
		if left_child < len(heap) and heap[left_child] < heap[smallest]:
			smallest = left_child
		if right_child < len(heap) and heap[right_child] < heap[smallest]:
			smallest = right_child
		if smallest != index:
			heap[index], heap[smallest] = heap[smallest], heap[index]
			index = smallest
		else:
			break


def print_min_heap_sorted(heap):
    heap_copy = heap.copy()  # Create a copy to avoid modifying the original heap
    sorted_list = []
	

# Example usage:
min_heap = [6, 3, 8, 5, 2, 9, 1, 4, 7]

print_min_heap_sorted(min_heap)



heap =[]
insert_min_heap(heap,2)
insert_min_heap(heap,200)
insert_min_heap(heap,212)
insert_min_heap(heap,1)

print(heap)

for _ in range(len(heap)):
	heap.pop(0)
	print(heap)