'''
We have a list of tasks to perform, with a cooldown period.
We can do multiple of these at the same time, but we cannot
run the same task simultaneously.

Given a list of tasks, find how long it will take to complete
the tasks in the order they are input.

tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
'''
from collections import defaultdict

def findTime(arr, cooldown):
    if not arr or cooldown < 0:
        return 0
    
    taskDict, taskList = defaultdict(int), []
    for task in arr:
        while True:
            for key in taskDict.keys():
                if taskDict[key] > 0:
                    taskDict[key] -= 1
                    
            if not taskList:
                taskList.append(task)
                taskDict[task] = cooldown + 1
                break
            
            if taskDict[task] == 0:
                taskList.append(task)
                taskDict[task] = cooldown + 1
                break
            else:
                taskList.append(0)
                
    return len(taskList)


if __name__ == '__main__':
    print(findTime([1, 1, 2, 1], 2))
