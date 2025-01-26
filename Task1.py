def rotate_array(arr, steps):
    steps %= len(arr)
    return arr[-steps:] + arr[:-steps]

arr = [1, 2, 3, 4, 5]
steps = 2
print("Output:", rotate_array(arr, steps))
