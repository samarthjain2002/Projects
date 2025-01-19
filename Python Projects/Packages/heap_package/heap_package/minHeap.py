class MinHeap:
    def __init__(self):
        self.minHeap = []

    def __len__(self):
        return len(self.minHeap)

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1
    
    def right_child(self, index):
        return (2 * index) + 2
    
    def swap(self, i, j):
        self.minHeap[i], self.minHeap[j] = self.minHeap[j], self.minHeap[i]


    # Also called sift-down
    def heapify_down(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index

        # Compare the current node with its children
        if left < len(self.minHeap) and self.minHeap[left] < self.minHeap[smallest]:
            smallest = left
        if right < len(self.minHeap) and self.minHeap[right] < self.minHeap[smallest]:
            smallest = right

        # Swap and continue heapifying if the smallest isn't the current node
        if smallest != index:
            self.swap(smallest, index)
            self.heapify_down(smallest)


    def heapify_up(self, index):
        parent = self.parent(index)
        if index > 0 and self.minHeap[index] < self.minHeap[parent]:
            self.swap(index, parent)
            self.heapify_up(parent)


    def heapify(self, arr):
        self.minHeap = arr[:]
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.heapify_down(i)


    def heappush(self, val):
        self.minHeap.append(val)
        self.heapify_up(len(self.minHeap) - 1)


    # Peek smallest (root) value without removing it
    def heappeek(self):
        if not self.minHeap:
            raise IndexError("Pop from an empty heap")
        return self.minHeap[0]


    def heappop(self):
        if not self.minHeap:
            raise IndexError("Pop from an empty heap")
        
        # Swap the root with the last element
        self.swap(0, -1)
        smallest = self.minHeap[-1]
        self.minHeap.pop()      # Remove last element, which was previously root (smallest)
        self.heapify_down(0)    # Heapify
        return smallest


    def display(self):
        print(self.minHeap)