'''
Blobs of various sizes are situated in a room. Each blob will move toward
the nearest smaller blob until it reaches it and engulfs it. After consumption,
the larger blob grows in size.

Your task is to create a class Blobservation (a portmanteau of blob and
observation) and methods that give information about each blob after an arbitrary
number of moves.
Class Details

A Blobservation class instance is instantiated with two integer values, h and w,
that represent the dimensions of the room. The instance methods are as follows:
populate

The populate method is called with an array/list representing a list of blobs.

    Each element is an object/dict (Map<String,Integer> in Java) with the
    following properties:
        x: vertical position
        y: horizontal position
        size: size of the blob
    This method may be called multiple times on the same class instance
    If a new blob's position is already occupied by an existing blob, the two
    fuse into a single blob
    If the list input contains any invalid values, discard it entirely and
    throw an error (do not update/modify the instance)

move

The move method may be called with up to one argument — a positive integer
representing the number of move iterations (ie. turns) to process. If no argument
is given, the integer value defaults to 1.
print_state

The print_state method is a nullary function that returns an array of the
positions and sizes of each blob at the current state (Java: a List<List<Integer>> ),
sorted in ascending order by x position, then by y. If there are no blobs, return
an empty array.

Blob Movement Behavior

With each turn, every blob whose size is larger than the smallest blob size
value will move to one of the 8 spaces immediately surrounding it (Moore neighborhood)
in the direction of the nearest target blob with a lower relative size.

    If a target's coordinates differ on both axes, the predatory blob will move
    diagonally. Otherwise, it will move in the cardinal direction of its target
    If multiple targets are at the same movement distance, the blob with the largest
    size is focused
    If there are multiple targets that have both the largest size and shortest
    movement distance, priority is set in clockwise rotation, starting from the 12 position
    If two blobs pass each other (e.g. swap positions as a result of their movement),
    they will not fuse
    Blobs of the smallest size remain stationary

Additional Technical Details

    A blob's initial size will range between 1 and 20
    Multiple blobs occupying the same space will automatically fuse into one
    When a blob consumes another blob, or when two blobs fuse, the remaining blob's
    size becomes the sum of the two
    The 2nd argument for the class constructor is optional; if omitted, the room
    defaults to a square, where w == h.
    Room dimensions (h and w) will range between 8 and 50
    Class instances will always be instantiated with valid arguments
    Methods should throw an error if called with invalid arguments
    Boolean values are not to be regarded as valid integers
    Python translation: Use Python 3 only

Example:
generation0 = [
    {'x':0,'y':4,'size':3},
    {'x':0,'y':7,'size':5},
    {'x':2,'y':0,'size':2},
    {'x':3,'y':7,'size':2},
    {'x':4,'y':3,'size':4},
    {'x':5,'y':6,'size':2},
    {'x':6,'y':7,'size':1},
    {'x':7,'y':0,'size':3},
    {'x':7,'y':2,'size':1}
]
blobs = Blobservation(8)
blobs.populate(generation0)
blobs.move()
blobs.print_state() #[[0,6,5],[1,5,3],[3,1,2],[4,7,2],[5,2,4],[6,7,3],[7,1,3],[7,2,1]]
blobs.move()
blobs.print_state() #[[1,5,5],[2,6,3],[4,2,2],[5,6,2],[5,7,3],[6,1,4],[7,2,4]]
blobs.move(1000)
blobs.print_state() #[[4,3,23]]
'''

class BlobError(Exception):
    pass

class Blob:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def distance(self, other):
        dx, dy = abs(self.x-other.x), abs(self.y-other.y)
        return dx + dy - min(dx, dy)    

class Blobservation:
    
    def __init__(self, height, width=0):
        if not 8 <= height <= 50:
            raise BlobError
        
        if width == 0:
            width = height
            
        if not 8 <= width <= 50:
            raise BlobError
        
        self.height = height
        self.width = width
        self.field = [[None]*width for _ in range(height)]
        self.blobs = []
    
    def populate(self, gen):
        def check_value(val, valmin, valmax):
            if type(val) is not int:
                raise BlobError
            
            if  not  valmin <= val <= valmax:
                raise BlobError

        for blob in gen:
            check_value(blob.get('x', -1), 0, self.height-1)
            check_value(blob.get('y', -1), 0, self.width-1)
            check_value(blob.get('size', 0), 1, 20)
            
        for f_blob in gen:
            x, y, size = f_blob['x'], f_blob['y'], f_blob['size']
            if self.field[x][y] is None:
                self.field[x][y] = Blob(x, y, size)
                self.blobs.append(self.field[x][y])
            else:
                self.field[x][y].size += size

    def get_cw_victim(self, blob, distance, size):
        off, arr = distance, []
        if blob.x-off >= 0:
            arr.extend(self.field[blob.x-off][blob.y:min(blob.y+1+off, self.width)])
            
        if blob.y+off < self.width:
            for i in range(blob.x-off, blob.x+off+1):
                if 0 <= i < self.height and self.field[i][blob.y+off] is not None:
                    arr.append(self.field[i][blob.y+off])

        if blob.x+off < self.height:
            arr.extend(self.field[blob.x+off][min(blob.y+1+off, self.width):max(blob.y-off, 0):-1])
            
        if blob.y-off >= 0:
            for i in range(blob.x+off, blob.x-off-1, -1):
                if 0 <= i < self.height and self.field[i][blob.y-off] is not None:
                    arr.append(self.field[i][blob.y-off])

        if blob.x-off >= 0:
            arr.extend(self.field[blob.x-off][min(blob.y-off, 0):blob.y])

        for t_blob in arr:
            if t_blob is not None and t_blob.size == size:
                return (off, t_blob)
            
        raise BlobError

    def get_victim(self, blob):
        dists = []
        for other in self.blobs:
            if other.size < blob.size:
                dists.append((blob.distance(other), other))
                
        dists.sort(key=lambda x: x[0])
        dists = [tpl for tpl in dists if tpl[0]==dists[0][0]]
        dists.sort(key=lambda x: x[1].size, reverse=True)
        if len(dists) > 1 and dists[0][1].size == dists[1][1].size:
            dists[0] = self.get_cw_victim(blob, dists[0][0], dists[0][1].size)
            
        return dists[0][1]

    def move(self, iterations=1):
        if type(iterations) != int or iterations < 1:
            raise BlobError
        
        for _ in range(iterations):
            if len(self.blobs) < 2:
                break
            
            min_size = min([b.size for b in self.blobs])
            step_field = [[[] for _ in range(self.width)] for _ in range(self.height)]
            for blob in self.blobs:
                blob.step_x, blob.step_y = 0, 0
                if blob.size == min_size:
                    continue
                
                victim_blob = self.get_victim(blob)
                
                if blob.x != victim_blob.x:
                    blob.step_x = (victim_blob.x-blob.x)//abs(victim_blob.x-blob.x)
                    
                if blob.y != victim_blob.y:
                    blob.step_y = (victim_blob.y-blob.y)//abs(victim_blob.y-blob.y)

            for blob in self.blobs:
                if blob.size == min_size:
                    continue
                
                blob.x += blob.step_x
                blob.y += blob.step_y
                step_field[blob.x][blob.y].append(blob)

            dead_blobs = []
            for i in range(self.height):
                for j in range(self.width):
                    if (self.field[i][j] is not None and
                        self.field[i][j].size==min_size):
                        step_field[i][j].append(self.field[i][j])

                    if step_field[i][j]:
                        dead_blobs.extend(step_field[i][j])
                        n_b = Blob(i, j, sum([b.size for b in step_field[i][j]]))
                        step_field[i][j] = n_b 
                        self.blobs.append(n_b)
                    else:
                        step_field[i][j] = None

            self.field = step_field
            for dead in dead_blobs:
                self.blobs.remove(dead)       
                                
    def print_state(self):
        blobs = []
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] is not None:
                    blobs.append([self.field[i][j].x,
                                  self.field[i][j].y,
                                  self.field[i][j].size])
        return blobs
 
if __name__ == '__main__':
    generation0 = [{'x':0,'y':4,'size':3},
                   {'x':0,'y':7,'size':5},
                   {'x':2,'y':0,'size':2},
                   {'x':3,'y':7,'size':2},
                   {'x':4,'y':3,'size':4},
                   {'x':5,'y':6,'size':2},
                   {'x':6,'y':7,'size':1},
                   {'x':7,'y':0,'size':3},
                   {'x':7,'y':2,'size':1}
                   ]
    blobs = Blobservation(8)
    blobs.populate(generation0)
    blobs.move()
    blobs.move()
    blobs.move(1000)
    print(blobs.print_state())

    
