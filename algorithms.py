
# Write your binary search algorithm (a function) and an efficient sorting algorithm (a function) here
def binary_search(items, lower, upper, target):
  while lower <= upper:
    middle = (lower + upper) // 2

    if items[middle] == target:
      return middle
    elif items[middle] > target:
      upper = middle - 1 
    else:
      lower = middle + 1

  return -1 

# quick sort function
def partition(items, left, right):
  middle = (left + right) // 2
  pivot = items[middle]
  items[middle], items[right] = items[right], items[middle]

  boundary = left 

  for ind in range(left, right):
    if items[ind] < pivot:
      items[ind], items[boundary] = items[boundary], items[ind]
      boundary += 1

  items[right], items[boundary] = items[boundary], items[right]
  return boundary

def quick_recurse(items, left, right):
  if left >= right:
    return 
  pivot_position = partition(items, left, right)
  quick_recurse(items, left, pivot_position-1)
  quick_recurse(items, pivot_position+1, right)

def quick_sort(items):
  quick_recurse(items, 0, len(items)-1)

def show_all(items):
  for indx, el in enumerate(items):
    print(f'{indx+1}:\n {el}')

test = [4,6,9,8,10,13,547,1034,6,43]
quick_sort(test)
# print(test)

find = binary_search(test, 0, len(test)-1, 13)
print(test)
print(find)