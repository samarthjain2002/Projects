from heap_package.minheap import MinHeap


print("MINHEAP")

# Create a MinHeap instance
heap = MinHeap()

# Insert elements
heap.heappush(10)
heap.heappush(4)
heap.heappush(15)
heap.heappush(20)
heap.heappush(0)

# Display the heap
print("Heap after insertions:")
heap.display()

# Peek the smallest element
print("Peek smallest element:", heap.heappeek())

# Pop the smallest element
print("Pop smallest element:", heap.heappop())
print("Heap after popping smallest:")
heap.display()

# Build a heap from an array
array = [7, 3, 9, 1, 6, 8]
heap.heapify(array)
print("Heap after building from array:")
heap.display()

# Pop all elements to demonstrate sorting
sorted_elements = []
while len(heap) > 0:
    sorted_elements.append(heap.heappop())
print("Sorted elements:", sorted_elements)




print("\n\n\n")

from heap_package.maxheap import MaxHeap


print("MAXHEAP")

# Create a MaxHeap instance
heap = MaxHeap()

# Insert elements
heap.heappush(10)
heap.heappush(4)
heap.heappush(15)
heap.heappush(20)
heap.heappush(0)

# Display the heap
print("Heap after insertions:")
heap.display()

# Peek the largest element
print("Peek largest element:", heap.heappeek())

# Pop the largest element
print("Pop largest element:", heap.heappop())
print("Heap after popping largest:")
heap.display()

# Build a heap from an array
array = [7, 3, 9, 1, 6, 8]
heap.heapify(array)
print("Heap after building from array:")
heap.display()

# Pop all elements to demonstrate sorting
sorted_elements = []
while len(heap) > 0:
    sorted_elements.append(heap.heappop())
print("Sorted elements in descending order:", sorted_elements)