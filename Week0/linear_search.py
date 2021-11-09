def linear_search(arr, k):
    for i, n in enumerate(arr):
        if n == k:
            print(f'{k} is present at {i} index of the array')
            return
    print(f'{k} not found in array')
