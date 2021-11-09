def insertion_sort(n):
    if n is None:
        raise TypeError('data cannot be none')
    if len(n) < 2:
        return n
    for i in range(1, len(n)):
        for j in range(i):
            if n[i] < n[j]:
                n[i], n[j] = n[j], n[i]
    return n


def main():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 11, 2, 32, 3, 234, 443]
    print(insertion_sort(n))


main()
