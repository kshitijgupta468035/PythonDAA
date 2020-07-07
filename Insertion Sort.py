# Function for insertion sort
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        # Compare between values in array
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        
        array[i+1] = key

size = int(input("Enter the length of the array: "))
input_array = []

# For loop for taking input from the user
for i in range(0, size):
    input_array.append(int(input("Enter Element: ")))

# Function call
insertion_sort(input_array)

# Print the final Output
print("\nFinal Array Sorted" , input_array)
