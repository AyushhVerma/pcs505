# O(n(log(n)))

if __name__ == "__main__":

    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    exists = False

    for i in l:
        d[i] = d.get(i, 0) + 1

    for i in d:
        if d[i] > n//2:
            print("yes")
            exists = True

    if not exists:
        print("No")

    new_l = list(sorted(l))

    if n & 1 == 0:
        print((new_l[n//2] + new_l[n//2+1]) // 2)
    else:
        print(new_l[n//2])
