f = open('d3_input.txt', 'r')
lines = f.readlines()

joltage = 0

def find_largest_k_digit_subsequence(s, k):
    if len(s) < k:
        return None
    result = []
    start = 0
    remaining = k
    while remaining > 0:
        end = len(s) - (remaining - 1)
        max_digit = max(s[start:end])
        pos = s.index(max_digit, start, end)
        result.append(max_digit)
        start = pos + 1
        remaining -= 1
    return ''.join(result)

for line in lines:
    line = line.strip()
    largest_12 = find_largest_k_digit_subsequence(line, 12)
    if largest_12:
        joltage += int(largest_12)

print('Joltage: ' + str(joltage))