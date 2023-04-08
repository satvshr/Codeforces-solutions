import math
n, m, a = map(int, input().split())

flagstone = math.ceil(n/a) * math.ceil(m/a)
print(flagstone)