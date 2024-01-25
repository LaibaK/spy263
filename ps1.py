'''
CSC263 Winter 2024
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# The bubbling down/up algorithm were inspired by La Vivien Post.
class MaxHeap:
    def __init__(self):
        self.data = []
        self.size = 0
        self.capacity = 1

    def bubble_down(self, location):
        item = self.data[location]
        pointer = 0
        not_reached = True
        while location < self.size//2 and not_reached:
            left = (2 * location) + 1
            right = (2 * location) + 2
            if right < self.size and self.data[left] < self.data[right]:
                pointer = right
            else:
                pointer = left
            self.data[location] = self.data[pointer]
            location = pointer	
            if item >= self.data[pointer]: # Reached the location we want to stop at
                not_reached = False
        self.data[location] = item

    def bubble_up(self, location: int):
        parent = (location - 1) // 2
        to_change = self.data[location]
        while location > 0 and  to_change > self.data[parent]:
            self.data[location] = self.data[parent]
            location = parent 
            parent = (parent-1) // 2	
        self.data[location] = to_change 
    

class MinHeap:
    def __init__(self):
        self.data = []
        self.size = 0
    def bubble_up(self, index):
        not_reached = True
        while index > 0 and not_reached:
            parent = (index - 1) // 2
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                not_reached = False

    def bubble_down(self, index):
      not_reached = True
      while not_reached:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left

        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest
        else:
            not_reached = False

def spy263(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of find_spy results
  '''
  max_heap = MaxHeap() # spy heap --> spy at root
  total = 0
  min_heap = MinHeap()
  results = []
  for command in commands:
    if command.split(" ")[0] == "insert":
        value = int(command.split(" ")[1]) # to be inserted to the data structure
        total+=1
        heap_insert(max_heap, min_heap, total, value)
    elif command == "find_spy":
       results.append(max_heap.data[0]) 
  return results

def heap_insert(max_heap: MaxHeap, min_heap: MinHeap, total, value):
    max_heap.capacity = (int(-1 * (total*0.263) // 1 * -1))
    if max_heap.size == 0: # if spy heap doesn't have any values, then the root is the smallest we have
        max_heap.data.append(value)
        max_heap.size += 1
        max_heap.capacity = (int(-1 * (total*0.263) // 1 * -1))
    elif max_heap.size >= 1 and max_heap.capacity == max_heap.size: # if we can't add any new nodes to the max_heap
        if value < max_heap.data[0]:
            min_heap.data.append(max_heap.data[0])
            max_heap.data[0] = value
            min_heap.size += 1
            max_heap.bubble_down(0) #bubble down
            min_heap.bubble_up(min_heap.size-1) #bubble up
        elif value > max_heap.data[0]:
            min_heap.data.append(value)
            min_heap.size += 1
            min_heap.bubble_up(min_heap.size-1) #bubble up
    elif max_heap.size >= 1 and max_heap.capacity > max_heap.size: # we can add a new node to our spy tree
        if min_heap.data[0] < value: # root of min heap is less than value
            max_heap.data.append(min_heap.data[0])
            min_heap.data[0] = value
            max_heap.size += 1
            min_heap.bubble_down(0)
            max_heap.bubble_up(max_heap.size-1)
        elif value < min_heap.data[0]:
            max_heap.data.append(value) #add to the last node, bring it up accordingly
            max_heap.size += 1
            max_heap.bubble_up(max_heap.size-1)

# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == '__main__':
  # some small test cases
  # Case 1 --> Random values
  assert [15, 6, 2] == spy263(
    ['insert 15',
    'find_spy',
    'insert 6',
    'insert 2',
    'insert 8',
    'find_spy',
    'insert -5',
    'insert -8',
    'insert 3',
    'insert 20',
    'find_spy'
    ])
  #Case 2 --> ascending, last value added is the smallest value
  assert [1, 2, 1] == spy263(
    ['insert 1',
       'insert 2',
       'find_spy',
       'insert 3',
       'insert 4',
       'insert 5',
       'find_spy',
       'insert -8',
       'find_spy'
      ])
  #Case 3 --> descending
  assert [1] == spy263(
      ['insert 5',
       'insert 4',
       'insert 3',
       'insert 2',
       'insert 1',
       'insert -8',
       'find_spy'
      ])
  #Case 4 --> Call spy twice in a row
  assert [1,1] == spy263(
      ['insert 5',
       'insert 4',
       'insert 3',
       'insert 2',
       'insert 1',
       'insert -8',
       'find_spy',
       'find_spy'
      ])
  
  #Case 5 --> Large list 
  assert [-23, -23, -7, -7, -7, -7, -7, -9, -9] == spy263(
    ['insert -23',
    'find_spy',
    'insert 14',
    'insert -7',
    'find_spy',
    'insert 31',
    'insert 18',
    'insert -2',
    'find_spy',
    'insert 8',
    'insert -10',
    'insert 25',
    'insert 5',
    'find_spy',
    'insert -15',
    'insert 12',
    'insert 36',
    'insert -4',
    'insert 9',
    'find_spy',
    'insert -20',
    'insert 27',
    'insert 3',
    'insert -6',
    'insert 17',
    'insert -30',
    'find_spy',
    'insert 22',
    'insert 7',
    'insert -13',
    'insert 40',
    'insert -1',
    'insert 11',
    'insert -25',
    'find_spy',
    'insert 16',
    'insert 2',
    'insert -9',
    'insert 33',
    'insert -18',
    'insert 6',
    'insert -11',
    'insert 29',
    'find_spy',
    'insert 1',
    'insert -22',
    'insert 10',
    'insert -5',
    'find_spy'
    ])

       