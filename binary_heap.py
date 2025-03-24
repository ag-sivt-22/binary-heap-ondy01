from dataclasses import dataclass

@dataclass
class Element:
    value = False
    priority = 0

class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _leva_odnoz(self, index):
        return 2 * index + 1
    
    def _prava_odnoz(self, index):
        return 2 * index + 2
    
    def _nahoru(self, index):
        while index > 0 and self.heap[index].priority < self.heap[self._parent(index)].priority:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)
    
    def _dolu(self, index):
        smallest = index
        leva = self._leva_odnoz(index)
        prava = self._prava_odnoz(index)
        
        if leva < len(self.heap) and self.heap[leva].priority < self.heap[smallest].priority:
            smallest = leva
        
        if prava < len(self.heap) and self.heap[prava].priority < self.heap[smallest].priority:
            smallest = prava
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._dolu(smallest)
    
    def push(self, element):
        self.heap.append(element)
        self._nahoru(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            raise Exception("Heap is empty")
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._dolu(0)
        
        return root
    
    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]

