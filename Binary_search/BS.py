import random
import time

def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low-high//2
    
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
             low=mid+1
        else:
            high=mid-1
    return -1

def generate_sorted_list(size):
    """Generates a large sorted list."""
    my_list = sorted(random.sample(range(size * 3), size)) # generate unique numbers and sort
    return my_list

dataset_size = 10_000_000  # Adjust for your needs
test_count = 10 # Number of tests to run

# Generate the massive sorted list
massive_list = generate_sorted_list(dataset_size)

# Test for values within the list
found_times = []
for _ in range(test_count):
    target_found = random.choice(massive_list) # pick a value that is in the list
    start_time = time.time()
    result = binary_search(massive_list, target_found)
    end_time = time.time()
    found_times.append(end_time - start_time)
    if result != -1:
        print(f"Found {target_found} at index {result}")
    else:
        print(f"Error: {target_found} should have been found.")

print(f"average time for found values: {sum(found_times)/len(found_times)}")

# Test for values not in the list
not_found_times = []
for _ in range(test_count):
    target_not_found = max(massive_list) + random.randint(1,1000) # pick a value that is not in the list.
    start_time = time.time()
    result = binary_search(massive_list, target_not_found)
    end_time = time.time()
    not_found_times.append(end_time - start_time)
    if result == -1:
        print(f"Correctly did not find {target_not_found}")
    else:
        print(f"Error: {target_not_found} should not have been found.")