def main() -> None:
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        l: list[int] = list(map(int, input().split()))[:n]
        target: int = int(input())
        count: int = 0
        
        for i in l:
            if abs(target - i) in l:
                count += 1
        
        print(count)

main()