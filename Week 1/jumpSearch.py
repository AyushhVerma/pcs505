def jump_search(A: list, k: int) -> int:
    
    prev: int = 0
    
    for i in range(0, len(A), int(len(A)**0.5)-1):        
        if A[i] >= k:
            for j in range(prev, i+1):
                if A[j] == k:
                    return j
            return -1
        prev = i
    
    return -1

def main() -> None:
    
    _list: list[int] = list(map(int, input().strip().split()))
    k: int = int(input())
    if (x := jump_search(_list, k)) != -1:
        print(f"Element {k} found at index: {x}")
    else:
        print(f"Element {k} doesn't exist in Array")

if __name__ == "__main__":
    main()
