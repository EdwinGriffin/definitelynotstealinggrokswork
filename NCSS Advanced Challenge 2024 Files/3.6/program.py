import csv

# Recursively search the list using a binary search
def recursive_binary_search(data, target, low, high):
  # Base case: target is not found within the range
  if low > high:
    return -1
  print(f'Checking between range of {data[low]} and {data[high]}')
  # Complete the function below
  

# Load data from a CSV file
def load_data(filename):
  numbers = []
  with open(filename, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
      for item in row:
        numbers.append(int(item.strip()))
  return numbers  

# Get the file name and target value from user
file_name = ("values.csv")
target = int(input("What's the value you want to search for: "))
# Load the data from the CSV file and sort it.
input_data = load_data(file_name)
input_data.sort()

# Perform the recursive binary search and output the result
result = recursive_binary_search(input_data, target, 0, len(input_data) - 1)
if result != -1:
  print(f'Target value of {target} was located in {file_name} at index {result}')
else:
  print(f'Target value {target} not located in file {file_name}')