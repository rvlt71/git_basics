#def check_words(word):
    #if "by you" in 
        #return word[word.index('')+1:]

with open('drume_boss_logs.txt', 'r') as f2:
    data = [line.strip() for line in f2]
    s = ''.join(data)
    
x = s.split(', ')

for word in s.split():
    if ('Drume') in word:    
        print(word)
