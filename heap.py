def build_max_heap(arr):
    n = len(arr)

    # Start from last parent and heapify all the way to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    return arr

def heapify(arr, n, i):
    largest = i        # Assume current i is largest
    left = 2 * i + 1    # Left child
    right = 2 * i + 2   # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Example usage:
arr = [4, 10, 3, 5, 1, 2, 7]
build_max_heap(arr)
print("Max Heap:", arr)

