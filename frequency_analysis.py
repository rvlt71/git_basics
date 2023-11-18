
f = open('testfile.txt')

lines = f.readlines()
print(lines)

print("Number of lines detected: ", len(lines))

#for line in lines :
#    print(line)


char_freq = {}
#print(char_freq)

for line in lines:
    print("The current line is: ", line)
    for letter in line:
        if letter in char_freq:
            char_freq[letter] += 1
        else:
            char_freq[letter] = 1

print(char_freq)