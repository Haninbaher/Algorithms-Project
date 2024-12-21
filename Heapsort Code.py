def heapify(arr, n, i):
    """Maintains the max-heap property."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_max_heap(arr):
    """Builds a max-heap from the array."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heapsort(arr):
    """Sorts the array using Heapsort."""
    n = len(arr)

    # Build a max-heap
    build_max_heap(arr)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage
numbers = [4, 10, 3, 5, 1]
heapsort(numbers)
print("Sorted array:", numbers)