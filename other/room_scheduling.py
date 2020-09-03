'''
You are given an array of tuples (start, end) representing time
intervals for lectures. The intervals may be overlapping.
Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
'''
def roomsCount(periods):
    maxRooms, localMax = 0, 0
    startTimes = sorted([prd[0] for prd in periods])
    endTimes = sorted([prd[1] for prd in periods])
    while startTimes and endTimes:
        if endTimes[0] > startTimes[0]:
            localMax += 1
            del startTimes[0]
            if localMax > maxRooms:
                maxRooms = localMax
        elif startTimes[0] > endTimes[0]:
            localMax -= 1
            del endTimes[0]
        else:
            del startTimes[0]
            del endTimes[0]
    return maxRooms


if __name__ == '__main__':
    print(roomsCount([(30, 75), (0, 50), (60, 150)]))
            
