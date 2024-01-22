'''
CSC263 Winter 2024
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def spy263(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of find_spy results
  Commands
  'insert x'
	    -Inserts the number x into the data structure in spy263
	    - Must take O(log n) time for worst case
  'find_spy'
	    On the data structure of size n, returns ceil(0.263*n)th smallest element
	    Must take O(1) time for worst case 
  '''
  pass # TODO: implement this function
  data_structure = []
  for command in commands:
    if command.split(" ")[0] == "insert":
      insert(data_structure, command.split(" ")[1])
    elif command.split(" ")[0] == "find_spy":
      find_spy(data_strucutre, len(data_structure))

def insert(data_structure,x):
  """
  inserts the number <x> into the <data strcture>
  """
  pass

def find_spy(data_structure, n):
  """
  On the <data structure> of size <n>, returns ceil(0.263*n)th smallest element
  """
  omega = 0.263

# You may add additional test case below. HOWEVER, your code must
# compile and be runnable in order to earn any credit for correctness.

if __name__ == '__main__':
  # some small test cases
  # Case 1
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
       'find_spy',
      ])

