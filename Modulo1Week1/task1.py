import sys

digit_string = sys.argv[1]
s = 0
for k in digit_string:
    s += int(k)
print(s)
