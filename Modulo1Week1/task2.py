import sys

num_steps = int(sys.argv[1])
for i in range(num_steps):
    print(" "*(num_steps - i - 1), end="")
    print("#"*(i + 1))
print()
