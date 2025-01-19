import unittest
from heap_package import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        """This method is called before every test."""
        self.min_heap = MinHeap()

    def test_empty_heap(self):
        """Test if the heap is empty at the start."""
        self.assertEqual(len(self.min_heap), 0)

    def test_insert_and_extract_min(self):
        """Test inserting elements and extracting the minimum element."""
        self.min_heap.insert(10)
        self.min_heap.insert(5)
        self.min_heap.insert(15)
        
        # Extract the minimum, which should be 5
        self.assertEqual(self.min_heap.extract_min(), 5)
        
        # The next minimum should be 10
        self.assertEqual(self.min_heap.extract_min(), 10)

    def test_heapify(self):
        """Test if heapify works correctly."""
        elements = [10, 5, 15, 20, 7, 30, 25]
        self.min_heap.heapify(elements)
        
        # After heapifying, the smallest element should be at the root
        self.assertEqual(self.min_heap.extract_min(), 5)

    def test_peek(self):
        """Test peeking the minimum element without extracting it."""
        self.min_heap.insert(10)
        self.min_heap.insert(5)
        self.assertEqual(self.min_heap.peek(), 5)

if __name__ == '__main__':
    unittest.main()