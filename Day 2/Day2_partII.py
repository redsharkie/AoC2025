def has_repeating_pattern(s):
    length = len(s)
    for n in range(2, length + 1):
        if length % n == 0:
            part_len = length // n
            parts = [s[i:i + part_len] for i in range(0, length, part_len)]
            if all(p == parts[0] for p in parts):
                return True
    return False

f = open('input.txt', 'r')
lines = f.readlines()
score = 0

for line in lines:
    line = line.strip()
    for entries in line.split(','):
        start, end = entries.split('-')
        i = int(start)
        while i <= int(end):
            s = str(i)
            if has_repeating_pattern(s):
                score += i
            i += 1

print('Score: ' + str(score))
