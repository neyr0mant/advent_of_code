import re
import heapq
from collections import defaultdict
list_data = [i for i in open("input.txt")]

def get_solve(data_in, part=1):
    pattern = re.compile(r'Step (.) must be finished before step (.) can begin\.')
    dep, pre, steps = defaultdict(set), defaultdict(set), set()
    for data in data_in:
        m = pattern.match(data)
        if m:
            a, b = m.groups()
            dep[a].add(b)
            pre[b].add(a)
            steps.update([a, b])
    if part == 1:
        available = [step for step in steps if not pre[step]]
        heapq.heapify(available)
        list_res = []
        while available:
            current = heapq.heappop(available)
            list_res.append(current)
            for dep_ in dep[current]:
                pre[dep_].remove(current)
                if not pre[dep_]:
                    heapq.heappush(available, dep_)
        result = "".join(list_res)
    else:
        # Время для каждого шага: 60 + позиция буквы
        def step_time(c):
            return 60 + (ord(c) - ord('A') + 1)
        available = [step for step in steps if not pre[step]]
        heapq.heapify(available)
        num_workers, current_time, completed = 5, 0, set()
        workers = [(0, None)] * num_workers
        while True:
            for i in range(num_workers):
                finish_time, task = workers[i]
                if task and finish_time == current_time:
                    completed.add(task)
                    for dependent in dep[task]:
                        pre[dependent].remove(task)
                        if not pre[dependent] and dependent not in completed:
                            heapq.heappush(available, dependent)
                    workers[i] = (0, None)
            for i in range(num_workers):
                if workers[i][1] is None:
                    if available:
                        next_task = heapq.heappop(available)
                        finish_time = current_time + step_time(next_task)
                        workers[i] = (finish_time, next_task)
            if len(completed) == len(steps):
                break
            ongoing_times = [w[0] for w in workers if w[1] is not None]
            current_time = min(ongoing_times)
        result = current_time
    return result

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")