f = open('input.txt', 'r')
lines = f.readlines()
score = 0

for line in lines:
    line = line.strip()
    for entries in line.split(','):
        start, end = entries.split('-')
        i = int(start)
        while i <= int(end):
            length = len(str(i))
            if (length% 2 == 0):
                first_half = str(i)[:length//2]
                second_half = str(i)[length//2:]
                if first_half == second_half:
                    score = score + i
            i += 1

print('Score: ' + str(score))
    