def main() -> None:

    test_cases: int = int(input())

    for _ in range(test_cases):

        n: int = int(input())
        l: list[int] = list(map(int, input().split()))[:n]
        found: bool = False

        for j in range(n-1, 0, -1):
            i = 0
            while i != j:
                print(i, j)
                diff = abs(l[j] - l[i])
                if diff in l:
                    found = True
                    break
                i += 1
            if found:
                break
        if found:
            print(f"{i+1}, {l.index(diff)+1}, {j+1}")
        else:
            print("No sequence found")

if __name__ == '__main__':
    main()