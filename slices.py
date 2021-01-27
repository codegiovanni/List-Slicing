# PYTHON SHORTS
# SLICES

 #                           +---+---+---+---+---+---+
 #                           | P | y | t | h | o | n |
 #                           +---+---+---+---+---+---+
 # Slice position:           0   1   2   3   4   5   6
 # Index position:             0   1   2   3   4   5
 # Reverse index position:    -6  -5  -4  -3  -2  -1
 # Reverse slice position:  -6  -5  -4  -3  -2  -1

s = ['P','y','t','h','o','n']
k = s[0]
print("k =", k)
l = s[1]
print("l =", l)

for i in s:
    print(i)

print("---------------------------------------------")

 # slicing gives lists
 # s[start:stop]  # items start through stop
 # s[start:]      # items start through the rest of the list
 # s[:stop]       # items from the beginning through stop
 # s[:]           # a copy of the whole list

print(s[:])
print(s[:2])
print(s[2:])
print(s[2:4])

print("---------------------------------------------")

# s[start:stop:step]  # items start through stop by step
print(s[::2])
print(s[::3])
print(s[1::3])

print("---------------------------------------------")

# negative indexing
print(s[-1])
print(s[-2])
print(s[-6])

print("---------------------------------------------")

# negative slicing
print(s[-2:])
print(s[-4:])
print(s[-6:-2])

# negative slicing with step
print(s[::-1]) # all items in the list reversed
print(s[-1:-6:-1])
print(s[-1:-7:-1])
print(s[1::-1])
print(s[4::-1])