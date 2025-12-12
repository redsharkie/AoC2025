f = open('d3_input.txt', 'r')
lines = f.readlines()

joltage = 0 

def find_max_number(s):
    s = (int(c) for c in s)
    return max(s)

for line in lines:
    line = line.strip()
    b1 = find_max_number(line[:-1])
    p = line.index(str(b1))
    b2 = find_max_number(line[p+1:])
    joltage += int(str(b1) + str(b2))

    
print('Joltage: ' + str(joltage))