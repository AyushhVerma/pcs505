if __name__ == "__main__":
    n = int(input())
    time_taken = list(map(int, input().split()))
    deadline = list(map(int, input().split()))
    time = [(time_taken[i], deadline[i], i) for i in range(n)]
    time.sort(key=lambda x:x[1])
    total_task_time = time[0][0]
    idx = 1
    acts = [1]
    while idx < n:
        if total_task_time + time[idx][0] <= time[idx][1]:
            acts.append(time[idx][2]+1)
            total_task_time += time[idx][0]
        idx += 1
    print(acts, len(acts))
