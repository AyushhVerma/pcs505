if __name__ == '__main__':
    n = int(input())
    start_time = list(map(int, input().split()))
    end_time = list(map(int, input().split()))
    tp = [i for i in zip(start_time, end_time)]
    tp.sort(key=lambda x:x[1])
    acts = []
    acts.append(1)
    idx = 1
    prev_end = tp[0][1]
    while idx < n-1:
        while tp[idx][0] < prev_end:
            idx += 1
        prev_end = tp[idx][1]
        acts.append(idx+1)
    print("No. of non-conflicting activities:", len(acts))
    print("List of selected activities:", acts)
