def binary_search(A: list, k: int, n: int) -> int:
    l_idx: int = 0
    r_idx: int = n - 1
    count: int = 1

    while l_idx <= r_idx:
        mid_idx = l_idx + (r_idx - l_idx) // 2
        if A[mid_idx] == k:
            mid_left = mid_idx - 1
            mid_right = mid_idx + 1
            while mid_right < n and A[mid_right] == k:
                mid_right += 1
                count += 1
            while mid_left > 0 and A[mid_left] == k:
                mid_left -= 1
                count += 1
            return count
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
        k: int = int(input())
        if (c := binary_search(array, k, len_of_array)) > 0:
            print(f"count: {c}")
        else:
            print(f"Element {k} doesn't exist in Array")

main()
