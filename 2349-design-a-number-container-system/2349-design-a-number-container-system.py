from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.index_number = {}  
        self.number_indices = {} 

    def change(self, index: int, number: int) -> None:
       
        if index in self.index_number:
            old_number = self.index_number[index]
            self.number_indices[old_number].discard(index)
            if not self.number_indices[old_number]:
                del self.number_indices[old_number] 

       
        self.index_number[index] = number
        if number not in self.number_indices:
            self.number_indices[number] = SortedSet()
        self.number_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_indices:
            return -1 
        return self.number_indices[number][0] 