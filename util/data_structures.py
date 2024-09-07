import heapq

class IndexedPriorityQueue:
    def __init__(self):
        self.heap = []  # Min-heap to store (priority, index)
        self.index_map = {}  # Map from index to position in the heap
        self.counter = 0  # Counter for tie-breaking in case of equal priorities

    def push(self, index, priority):
        if index in self.index_map:
            self.update(index, priority)
        else:
            entry = (priority, self.counter, index)
            self.index_map[index] = entry
            heapq.heappush(self.heap, entry)
            self.counter += 1

    def pop(self):
        while self.heap:
            priority, _, index = heapq.heappop(self.heap)
            # Check if the current entry is the most recent one for this index
            if index in self.index_map and self.index_map[index] == (priority, _, index):
                del self.index_map[index]
                return index, priority
        raise KeyError("Pop from an empty priority queue")

    def update(self, index, new_priority):
        if index in self.index_map:
            old_entry = self.index_map.pop(index)
            new_entry = (new_priority, self.counter, index)
            heapq.heappush(self.heap, new_entry)
            self.index_map[index] = new_entry
            self.counter += 1
        else:
            self.push(index, new_priority)

    def remove(self, index):
        if index in self.index_map:
            del self.index_map[index]
        else:
            raise KeyError(f"Index {index} not found in the priority queue")

    def is_empty(self):
        return len(self.index_map) == 0

    def contains(self, index):
        return index in self.index_map

    def get_priority(self, index):
        if index in self.index_map:
            return self.index_map[index][0]
        raise KeyError(f"Index {index} not found in the priority queue")
