def binary_search(A: list, k: int, n: int) -> int:
    l_idx = 0
    r_idx = n - 1
    
    while l_idx <= r_idx:
    
        mid_idx = l_idx + (r_idx - l_idx) // 2
        if A[mid_idx] == k:
            return mid_idx
        elif k > A[mid_idx]:
            l_idx = mid_idx + 1
        else:
            r_idx = mid_idx - 1
    
    return 0

def main() -> None:

    test_cases: int = int(input())
    for _ in range(test_cases):

        len_of_array: int = int(input())
        array: list[int] = list(map(int, input().strip().split()))[:len_of_array]
        k = int(input())

        if (idx := binary_search(array, k, len_of_array)) > 0:
            print(f"Element {k} found at index: {idx}")
        else:
            print(f"Element {k} doesn't exist in Array")

if __name__ == '__main__':
    main()
