startposition = 50
pos = startposition
password = 0   

f = open('input copy.txt', 'r')
lines = f.readlines()

def rotate_position(pos, direction, steps):
    nr_of_rounds = 0
    if len(str(steps)) > 2:
        # Beperk stappen tot de laatste 2 cijfers
        print('org steps ' + str(steps))
        print('org nr of rounds ' + str(nr_of_rounds))

        nr_of_rounds += int(str(steps)[::-1][2:][::-1])
        print('new nr of rounds ' + str(nr_of_rounds))
        steps = int(str(steps)[::-1][:2][::-1])
        print('new steps ' + str(steps))
    if direction == 'L':
        pos -= steps
        if pos < 0:
               pos = 100 - abs(pos)  
               nr_of_rounds += 1
    elif direction == 'R':
        pos += steps
        if pos >= 100:
               pos= int(str(pos)[1:])
               nr_of_rounds += 1
    print('Steps: ' + str(steps))
    print('Direction: ' + direction)
    print('Pos: ' + str(pos))
    print('Nr of rounds: ' + str(nr_of_rounds))
    pos = pos
    return pos


for line in lines:
    direction = line[0]
    steps = int(line[1:])
    pos = rotate_position(pos, direction, steps)
    if pos == 0:
        password += 1

print('Password: ' + str(password))

