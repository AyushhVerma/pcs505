def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        arr[i], arr[r] = arr[r], arr[i]
    return i

def kth_smallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return kth_smallest(arr, l, index - 1, k)
        return kth_smallest(arr, index + 1, r,
                k - index + l - 1)
    print("Index out of bound")

arr = [ 10, 4, 5, 8, 6, 11, 26 ]

n = len(arr)
k = 3

print("K-th smallest element is ", end = "")
print(kth_smallest(arr, 0, n - 1, k))
