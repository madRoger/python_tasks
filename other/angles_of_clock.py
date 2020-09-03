'''
Given a time in the format of hour and minute,
calculate the angle of the hour and minute hand on a clock.
'''
def calcAngle(h, m):
    h = h % 12
    m = m % 60
    mAngle = 6 * m
    hAngle = 30*h + m/2
    return (mAngle - hAngle) if mAngle > hAngle else (360 - (hAngle - mAngle))
    
if __name__ == '__main__':
    print(calcAngle(3, 30))
    print(calcAngle(12, 30))
