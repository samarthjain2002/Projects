def import_heaps():
    from .minheap import MinHeap
    from .maxheap import MaxHeap
    return MinHeap, MaxHeap

MinHeap, MaxHeap = import_heaps()

__all__ = ["MinHeap", "MaxHeap"]