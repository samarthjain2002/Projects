import unittest
from heap_package import MaxHeap

class TestMaxHeap(unittest.TestCase):

    def setUp(self):
        """This method is called before every test."""
        self.max_heap = MaxHeap()

    def test_empty_heap(self):
        """Test if the heap is empty at the start."""
        self.assertEqual(len(self.max_heap), 0)

    def test_insert_and_extract_max(self):
        """Test inserting elements and extracting the maximum element."""
        self.max_heap.heappush(10)
        self.max_heap.heappush(5)
        self.max_heap.heappush(15)
        
        # Extract the maximum, which should be 15
        self.assertEqual(self.max_heap.heappop(), 15)
        
        # The next maximum should be 10
        self.assertEqual(self.max_heap.heappop(), 10)

    def test_heapify(self):
        """Test if heapify works correctly."""
        elements = [10, 5, 15, 20, 7, 30, 25]
        self.max_heap.heapify(elements)
        
        # After heapifying, the largest element should be at the root
        self.assertEqual(self.max_heap.heappop(), 30)

    def test_peek(self):
        """Test peeking the maximum element without extracting it."""
        self.max_heap.heappush(10)
        self.max_heap.heappush(5)
        self.assertEqual(self.max_heap.heappeek(), 10)

if __name__ == '__main__':
    unittest.main()