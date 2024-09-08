import time
import json

# capture the approximate start time of this program running
start_time = time.time()

def sort_customers(customer_dictionary):
  # Replace the pass statement with code to sort the dictionary
  # and return it
  pass
  
def check_efficient_duration(duration):
  # Replace the pass statement to check if the duration
  # is considered efficient or not (according to numbers in 
  # the problem description) and return True/False accordingly
  pass

def print_dictionary(dictionary):
  ''' Function for printing out the dictionary, assuming it's been sorted already. '''
  for customer, pets in dictionary.items():
    if pets:
      print(f"{customer}: {', '.join(pets)}")
    else:
      print(f"{customer}: No pets")
        
    
# Use this to test your program. This code will be 
# ignored by the marker when testing your functions
if __name__ == '__main__':
  with open('vet_customers.json') as f:
    customers = json.load(f)
  sorted_customers = sort_customers(customers)
  print_dictionary(sorted_customers)

  end_time = time.time()
  duration = end_time - start_time
  is_efficient_algorithm = check_efficient_duration(duration)
  print()
  if is_efficient_algorithm:
    print('Efficient time complexity based on small data sample.')
  else:
    print('Not the most efficient algorithm!')