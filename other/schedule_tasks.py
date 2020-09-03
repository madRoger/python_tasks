'''
A task is a some work to be done which can be assumed takes 1 unit of time.
Between the same type of tasks you must take at least n units of time before
running the same tasks again.

Given a list of tasks (each task will be represented by a string),
and a positive integer n representing the time it takes to run the
same task again, find the minimum amount of time needed to run all tasks.
'''
from collections import Counter

def schedule_tasks(tasks, n):
    cnt, shedule = Counter(tasks), []
    while cnt:
        for task, _ in cnt.most_common(n):
            shedule.append(task)
            cnt[task] -= 1
            
        if len(cnt) < n:
            shedule.extend(['idle'] * (n - len(cnt)))
            
        deltasks = []
        for task, count in cnt.items():
            if not count:
                deltasks.append(task)
                
        for deltask in deltasks:
            del cnt[deltask]
            
    while shedule[-1] == 'idle':
        shedule.pop()
        
    return len(shedule)

if __name__ == '__main__':
    print(schedule_tasks(['q', 'q', 'q', 'w', 'w', 's', 't', 'k'], 2))
