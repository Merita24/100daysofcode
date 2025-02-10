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

test_count=5
dataset_size=5000
def generate_dataset(size):
  my_list=sorted(random.sample(range(size*3),size))
  return my_list
my_dataset=generate_dataset(dataset_size)

found_time=[]
for i in test_count:
  target_found=random.choice(my_dataset)
  start_time=time.time()
  result=binary_search(my_dataset,target_found)
  end_time=time.time()
  found_time.append(end_time-start_time)
if result != -1:
        print(f"Found {target_found} at index {result}")
else:
        print(f"Error: {target_found} should have been found.")


no_found_time=[]
target_not_found=max(my_dataset)+random.randint(1,100)
start_time=time.time()
result=binary_search(my_dataset,target_not_found)
end_time=time.time()
no_found_time.append(end_time-start_time)
if result == -1:
        print(f"Correctly did not find {target_not_found}")
else:
        print(f"Error: {target_not_found} should not have been found.")