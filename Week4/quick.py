def quick_sort(n):
    if len(n) < 2:
        return n
    pivot = n[len(n)//2]
    left = []
    equal = []
    right = []
    for i in n:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            right.append(i)
    re_left = quick_sort(left)
    re_right = quick_sort(right)
    return re_left + equal + re_right


def main():
    n = list(map(int, input().strip().split()))
    print(quick_sort(n))


main()
