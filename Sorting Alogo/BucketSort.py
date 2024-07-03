def bucket_sort(arr):
    # Step 1: Create empty buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        index = int(num * n)  # Index in bucket
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for bucket in buckets:
        bucket.sort()  # You can use any sorting algorithm here

    # Step 4: Concatenate buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
