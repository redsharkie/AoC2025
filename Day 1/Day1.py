startposition = 50
pos = startposition
password = 0   

f = open('input.txt', 'r')
lines = f.readlines()

def rotate_position(pos, direction, steps):
    if len(str(steps)) > 2:
        # Beperk stappen tot de laatste 2 cijfers
        steps = int(str(steps)[::-1][:2][::-1])
 
    if direction == 'L':
        pos -= steps
        if pos < 0:
               pos = 100 - abs(pos)  
    elif direction == 'R':
        pos += steps
        if pos >= 100:
               pos= int(str(pos)[1:])
    return pos 


for line in lines:
    direction = line[0]
    steps = int(line[1:])
    pos = rotate_position(pos, direction, steps)
    if pos == 0:
        password += 1

print('Password: ' + str(password))

