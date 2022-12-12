def merge_sort(array):
  if len(array) <= 1:
    return array
  
  # Divide the array into two equal-sized sub-lists
  mid = len(array) // 2
  left_list = array[:mid]
  right_list = array[mid:]
  
  # Recursively sort each sub-list
  left_list = merge_sort(left_list)
  right_list = merge_sort(right_list)
  
  # Merge the sorted sub-lists together
  return merge(left_list, right_list)

def merge(left_list, right_list):
  sorted_list = []
  
  # Iterate through the left and right lists and add the smaller element to the sorted list
  while len(left_list) > 0 and len(right_list) > 0:
    if left_list[0] <= right_list[0]:
      sorted_list.append(left_list[0])
      left_list = left_list[1:]
    else:
      sorted_list.append(right_list[0])
      right_list = right_list[1:]
  
  # Add the remaining elements of the left list to the sorted list
  if len(left_list) > 0:
    sorted_list.extend(left_list)
  
  # Add the remaining elements of the right list to the sorted list
  if len(right_list) > 0:
    sorted_list.extend(right_list)
  
  return sorted_list

# Test the merge_sort function
print(merge_sort([4, 6, 2, 5, 1, 3]))   # [1, 2, 3, 4, 5, 6]
