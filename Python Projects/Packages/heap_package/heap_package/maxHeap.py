class MaxHeap:
    def __init__(self):
        self.maxHeap = []

    def __len__(self):
        return len(self.maxHeap)

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def swap(self, i, j):
        self.maxHeap[i], self.maxHeap[j] = self.maxHeap[j], self.maxHeap[i]


    # Restore the heap property by bubbling down
    def heapify_down(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        largest = index

        # Compare the current node with its children
        if left < len(self.maxHeap) and self.maxHeap[left] > self.maxHeap[largest]:
            largest = left
        if right < len(self.maxHeap) and self.maxHeap[right] > self.maxHeap[largest]:
            largest = right

        # Swap and continue heapifying if the largest isn't the current node
        if largest != index:
            self.swap(largest, index)
            self.heapify_down(largest)


    # Restore the heap property by bubbling up
    def heapify_up(self, index):
        parent = self.parent(index)
        if index > 0 and self.maxHeap[index] > self.maxHeap[parent]:
            self.swap(index, parent)
            self.heapify_up(parent)


    def heapify(self, arr):
        self.maxHeap = arr[:]
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.heapify_down(i)


    def heappush(self, val):
        self.maxHeap.append(val)
        self.heapify_up(len(self.maxHeap) - 1)


    # Peek the largest (root) value without removing it
    def heappeek(self):
        if not self.maxHeap:
            raise IndexError("Peek from an empty heap")
        return self.maxHeap[0]


    def heappop(self):
        if not self.maxHeap:
            raise IndexError("Pop from an empty heap")

        # Swap the root with the last element
        self.swap(0, len(self.maxHeap) - 1)
        largest = self.maxHeap.pop()  # Remove last element, which was previously the root
        self.heapify_down(0)  # Restore the heap property
        return largest


    def display(self):
        print(self.maxHeap)