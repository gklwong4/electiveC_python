def binary_search(arr, target):
    global compCount
    left, right = 0, len(arr) - 1

    while ___________________:
        mid =_______________________________
        
        compCount += 1
      
        # Check if target is present at mid
        if arr[mid] == ______________:
            return mid  # Target found

        # If target is greater, ignore left half
        elif _______________________:
            __________ = _______________

        # If target is smaller, ignore right half
        else:
            _____________ = _______________

    return -1  # Target not found


# Generate an array of ntegers and sort it
import random
compCount = 0
array = sorted(random.sample(range(1, 101), 32))
print("Sorted Array:", array)

target = int(input("Enter an integer to search for: "))
result = binary_search(array, target)

if result != -1:
    print(f"Target found at index {result}.")
else:
    print("Target not found.")

print(f'No. of comparisons = {compCount}')
