'''
Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
'''
def make_readable(seconds):
    hours = seconds // 3600
    mins = (seconds - hours*3600) // 60
    secs = seconds - hours*3600 - mins*60
    return '{0:02}:{1:02}:{2:02}'.format(hours, mins, secs)
 
if __name__ == '__main__':
    print(make_readable(36521))
    
