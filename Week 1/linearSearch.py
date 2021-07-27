def linear_search(A: list, k: int) -> int:
    
    for i in range(len(A)):
        if A[i] == k:
            return i
    return -1
    
def main() -> None:
    
    _list: list[int] = list(map(int, input().strip().split()))
    k: int = int(input())
    
    if (x := linear_search(_list, k)) != -1:
        print(f"Element {k} present at index: {x}")
    else:
        print(f"Element {k} doesn't exist in Array")

if __name__ == '__main__':
    main()