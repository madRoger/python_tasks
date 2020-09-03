'''
A multi-floor building has a Lift in it.

People are queued on different floors waiting for the Lift.
Some people want to go up. Some people want to go down.
The floor they want to go to is represented by a number
(i.e. when they enter the Lift this is the button they will press)

BEFORE (people waiting in queues)               AFTER (people at their destinations)
                   +--+                                          +--+ 
  /----------------|  |----------------\        /----------------|  |----------------\
10|                |  | 1,4,3,2        |      10|             10 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 9|                |  | 1,10,2         |       9|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 8|                |  |                |       8|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 7|                |  | 3,6,4,5,6      |       7|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 6|                |  |                |       6|          6,6,6 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 5|                |  |                |       5|            5,5 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 4|                |  | 0,0,0          |       4|          4,4,4 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 3|                |  |                |       3|            3,3 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 2|                |  | 4              |       2|          2,2,2 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 1|                |  | 6,5,2          |       1|            1,1 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 G|                |  |                |       G|          0,0,0 |  |                |
  |====================================|        |====================================|

Rules
Lift Rules

    The Lift only goes up or down!
    Each floor has both UP and DOWN Lift-call buttons (except top and ground floors
    which have only DOWN and UP respectively)
    The Lift never changes direction until there are no more people wanting to get
    on/off in the direction it is already travelling
    When empty the Lift tries to be smart. For example,
        If it was going up then it may continue up to collect the highest floor person
        wanting to go down
        If it was going down then it may continue down to collect the lowest floor person
        wanting to go up
    The Lift has a maximum capacity of people
    When called, the Lift will stop at a floor even if it is full, although unless somebody
    gets off nobody else can get on!
    If the lift is empty, and no people are waiting, then it will return to the ground floor

People Rules

    People are in "queues" that represent their order of arrival to wait for the Lift
    All people can press the UP/DOWN Lift-call buttons
    Only people going the same direction as the Lift may enter it
    Entry is according to the "queue" order, but those unable to enter do not block those
    behind them that can
    If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call
    button again after it has departed without them
'''
from itertools import cycle

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = list(map(list, queues))
        self.capacity = capacity

    def theLift(self):
        floors = len(self.queues) - 1
        track = [(True, x) for x in range(floors)]
        track.extend([(False, x) for x in range(floors, 0, -1)])
        lift, path = [], [0]
        for up, floor in cycle(track):
            if floor in lift:
                lift = [man for man in lift if man != floor]
                path.append(floor)
                
            if floor == 0 and not lift and not any(self.queues):
                break
            
            crowd = list(filter(lambda x: x>floor if up else x<floor, self.queues[floor]))
            if crowd and path[-1] != floor:
                path.append(floor)
                
            for man in crowd:
                if len(lift) == self.capacity:
                    break
                
                lift.append(man)
                self.queues[floor].remove(man)
                
        if path[-1] != 0:
            path.append(0)
            
        return path

 
if __name__ == '__main__':
    mouse = Dinglemouse(((), (), (5,5,5), (), (), (), ()), 7)
    print(mouse.theLift())

    
