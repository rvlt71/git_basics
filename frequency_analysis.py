f = open('testfile.txt')

lines = f.readlines()
print(lines)

for y in lines :
    print(y)
    print(len(lines))

char_freq = {}
print(char_freq)

for x in f :
    print(x)
    if x in char_freq:
        char_freq[x] += 1
    else:
        char_freq[x] = 1

print(char_freq)