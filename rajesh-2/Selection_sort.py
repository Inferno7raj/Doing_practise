def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


input_str = input("Enter up to 10 numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()][:10]  # Limit to 10 elements

sorted_list = selection_sort(input_list)
print("Sorted list:", sorted_list)
