def merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result


def sort(n):
    if len(n) < 2:
        return n
    mid = len(n) // 2
    l = sort(n[:mid])
    r = sort(n[mid:])
    return merge(l, r)


def main():
    n = list(map(int, input().split()))
    print(sort(n))


main()
